import random
import itertools
from flask import Flask, jsonify, render_template, request

# --- Flask App Initialization ---
app = Flask(__name__)

# --- Game State Management ---
# We'll store the game state in memory instead of a file.
# This is simpler for a web server context.
game_state = {
    'open_tiles': list(range(1, 13)),
    'current_roll': [],
    'roll_sum': 0,
    'is_game_over': False,
    'message': "Roll the dice to start!",
    'won': False
}

# --- CORE DICE FUNCTIONS (Adapted for Web) ---
def roll_multiple_dice(num_dice, num_sides=6):
    """Rolls multiple dice and returns a list of results."""
    return [random.randint(1, num_sides) for _ in range(num_dice)]

# --- SHUT THE BOX LOGIC (Unchanged) ---
def is_move_possible(open_tiles, roll_sum):
    """Checks if any combination of open tiles sums to the roll."""
    for i in range(1, len(open_tiles) + 1):
        for combo in itertools.combinations(open_tiles, i):
            if sum(combo) == roll_sum:
                return True
    return False

# --- API Endpoints ---

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

# --- API for the Generic Dice Roller ---
@app.route('/roll/<spec>')
def handle_dice_roll(spec):
    """Handles requests like /roll/2d6"""
    try:
        if 'd' not in spec:
            raise ValueError("Invalid format")
        
        parts = spec.lower().split('d')
        num_dice = int(parts[0]) if parts[0] else 1
        num_sides = int(parts[1])

        if num_dice < 1 or num_sides < 1:
            raise ValueError("Dice and sides must be positive")

        results = roll_multiple_dice(num_dice, num_sides)
        return jsonify({
            'ok': True,
            'spec': f"{num_dice}d{num_sides}",
            'results': results,
            'sum': sum(results)
        })
    except (ValueError, IndexError):
        return jsonify({
            'ok': False,
            'error': "Invalid format. Please use 'XdY', e.g., '2d6'."
        }), 400


# --- API for Shut The Box Game ---

@app.route('/game/state', methods=['GET'])
def get_game_state():
    """Returns the current state of the Shut the Box game."""
    return jsonify(game_state)

@app.route('/game/new', methods=['POST'])
def new_game():
    """Resets the game to its initial state."""
    global game_state
    game_state = {
        'open_tiles': list(range(1, 13)),
        'current_roll': [],
        'roll_sum': 0,
        'is_game_over': False,
        'message': "New game started. Roll the dice!",
        'won': False
    }
    return jsonify(game_state)

@app.route('/game/roll', methods=['POST'])
def game_roll():
    """Rolls the dice for the Shut the Box game."""
    if game_state['is_game_over']:
        return jsonify({'ok': False, 'error': 'Game is over. Start a new game.'}), 400

    roll = roll_multiple_dice(2, 6)
    roll_sum = sum(roll)
    game_state['current_roll'] = roll
    game_state['roll_sum'] = roll_sum

    if not is_move_possible(game_state['open_tiles'], roll_sum):
        game_state['is_game_over'] = True
        final_score = sum(game_state['open_tiles'])
        game_state['message'] = f"Game Over! No possible moves. Final Score: {final_score}"
    else:
        game_state['message'] = f"You rolled {roll} (Sum: {roll_sum}). Select tiles to shut."

    return jsonify(game_state)

@app.route('/game/move', methods=['POST'])
def game_move():
    """Handles a player's move to shut tiles."""
    if game_state['is_game_over']:
        return jsonify({'ok': False, 'error': 'Game is over. Start a new game.'}), 400

    data = request.get_json()
    chosen_tiles = data.get('tiles', [])

    # --- Input Validation ---
    if not chosen_tiles:
        return jsonify({'ok': False, 'error': 'No tiles were selected.'}), 400
    
    if sum(chosen_tiles) != game_state['roll_sum']:
        return jsonify({'ok': False, 'error': 'Sum of tiles does not match roll sum.'}), 400

    if not all(tile in game_state['open_tiles'] for tile in chosen_tiles):
        return jsonify({'ok': False, 'error': 'Invalid tile chosen.'}), 400
    
    # --- Process Valid Move ---
    for tile in chosen_tiles:
        game_state['open_tiles'].remove(tile)
    
    game_state['current_roll'] = []
    game_state['roll_sum'] = 0
    game_state['message'] = "Move successful! Roll the dice again."

    # --- Win Condition Check ---
    if not game_state['open_tiles']:
        game_state['is_game_over'] = True
        game_state['won'] = True
        game_state['message'] = "Congratulations! You have Shut the Box! 🎉"

    return jsonify(game_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
