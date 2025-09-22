from flask import Flask, render_template, request, jsonify
import os
from game_logic import (
    roll_multiple_dice, roll_single_die,
    load_game, save_game, is_move_possible
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# --- Dice Roller ---
@app.route("/roll_custom", methods=["POST"])
def roll_custom():
    data = request.json
    command = data.get("command", "").lower().strip()

    if not command.startswith("roll"):
        return jsonify({"error": "Invalid command"}), 400

    parts = command.split()

    if len(parts) == 1:
        result = roll_single_die()
        return jsonify({"results": [result], "sum": result})

    elif len(parts) == 2 and 'd' in parts[1]:
        try:
            dice_spec = parts[1].split('d')
            num_dice = int(dice_spec[0]) if dice_spec[0] else 1
            num_sides = int(dice_spec[1])

            if num_dice < 1 or num_sides < 1:
                return jsonify({"error": "Number of dice and sides must be positive"}), 400

            results = roll_multiple_dice(num_dice, num_sides)
            return jsonify({"results": results, "sum": sum(results)})

        except (ValueError, IndexError):
            return jsonify({"error": "Invalid format. Use 'roll XdY', e.g., 'roll 2d6'"}), 400

    else:
        return jsonify({"error": "Invalid 'roll' command"}), 400

# --- Shut the Box ---
@app.route("/start_shutbox", methods=["POST"])
def start_shutbox():
    tiles = list(range(1, 13))
    save_game(tiles)
    return jsonify({"tiles": tiles})

@app.route("/roll_shutbox", methods=["POST"])
def roll_shutbox():
    tiles = load_game()
    roll = roll_multiple_dice(2, 6)
    roll_sum = sum(roll)
    possible = is_move_possible(tiles, roll_sum)
    return jsonify({"roll": roll, "sum": roll_sum, "possible": possible, "tiles": tiles})

@app.route("/move_shutbox", methods=["POST"])
def move_shutbox():
    data = request.json
    chosen_tiles = data.get("chosen_tiles", [])
    roll_sum = data.get("roll_sum")
    tiles = load_game()

    if not all(tile in tiles for tile in chosen_tiles):
        return jsonify({"error": "Invalid tiles"}), 400
    if sum(chosen_tiles) != roll_sum:
        return jsonify({"error": "Sum mismatch"}), 400

    for tile in chosen_tiles:
        tiles.remove(tile)
    save_game(tiles)

    return jsonify({"tiles": tiles, "win": len(tiles) == 0})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)