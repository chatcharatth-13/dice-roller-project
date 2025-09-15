import random
import itertools

# --- CORE DICE FUNCTIONS (Unchanged) ---
def roll_single_die(num_sides=6):
    """
    Rolls a single die with a specified number of sides.
    Defaults to a 6-sided die if num_sides is not provided.
    """
    if not isinstance(num_sides, int) or num_sides < 1:
        raise ValueError("Number of sides must be a positive integer.")
    return random.randint(1, num_sides)

def roll_multiple_dice(num_dice, num_sides=6):
    """
    Rolls multiple dice, each with a specified number of sides.
    Returns a list of results.
    """
    if not isinstance(num_dice, int) or num_dice < 1:
        raise ValueError("Number of dice must be a positive integer.")

    results = []
    for _ in range(num_dice):
        results.append(roll_single_die(num_sides))
    return results

# --- SHUT THE BOX MINI-GAME (Unchanged) ---
def is_move_possible(open_tiles, roll_sum):
    """Checks if any combination of open tiles sums to the roll."""
    for i in range(1, len(open_tiles) + 1):
        for combo in itertools.combinations(open_tiles, i):
            if sum(combo) == roll_sum:
                return True
    return False

def play_shut_the_box():
    """Main function to play a game of Shut the Box."""
    tiles = list(range(1, 10))
    print("\n--- Welcome to Shut the Box! ---")
    print("Goal: Flip down all tiles. Your turn ends when you can't match your roll.")

    while True:
        print(f"\nOpen tiles: {tiles}")
        num_dice = 2 if sum(tiles) > 6 else 1
        roll = roll_multiple_dice(num_dice, 6)
        roll_sum = sum(roll)
        print(f"You rolled: {roll} (Sum: {roll_sum})")

        if not is_move_possible(tiles, roll_sum):
            print(f"No possible moves for a roll of {roll_sum}. Game Over!")
            print(f"Your final score (sum of remaining tiles): {sum(tiles)}")
            break

        while True:
            try:
                choice_str = input("Enter tiles to shut, separated by spaces: ")
                if not choice_str: continue # Handle empty input
                chosen_tiles = [int(n) for n in choice_str.split()]

                if sum(chosen_tiles) != roll_sum:
                    print(f"Error: The sum of your chosen tiles ({sum(chosen_tiles)}) does not match the roll sum ({roll_sum}). Try again.")
                elif not all(tile in tiles for tile in chosen_tiles):
                    print("Error: You chose a tile that is already shut. Try again.")
                else:
                    for tile in chosen_tiles:
                        tiles.remove(tile)
                    break 
            except ValueError:
                print("Invalid input. Please enter numbers separated by spaces.")

        if not tiles:
            print("\nCongratulations! You have Shut the Box! 🎉")
            break
    print("Returning to the main menu...")

# --- NEW FUNCTION TO HANDLE THE DICE ROLLING MODE ---
def handle_dice_rolling():
    """Manages the dice rolling interface."""
    print("\n--- Dice Roller ---")
    print("Type 'roll XdY' to roll X dice with Y sides (e.g., 'roll 2d6').")
    print("Type 'roll' to roll a single 6-sided die.")
    print("Type 'back' to return to the main menu.")

    while True:
        user_input = input("\nEnter roll command: ").lower().strip()

        if user_input == 'back':
            print("Returning to the main menu...")
            break
        elif user_input.startswith('roll'):
            parts = user_input.split()

            if len(parts) == 1: # Just 'roll'
                print(f"Rolling 1d6: {roll_single_die()}")
            elif len(parts) == 2 and 'd' in parts[1]:
                try:
                    dice_spec = parts[1].split('d')
                    num_dice = int(dice_spec[0]) if dice_spec[0] else 1
                    num_sides = int(dice_spec[1])

                    if num_dice < 1 or num_sides < 1:
                        print("Invalid input: Number of dice and sides must be positive.")
                        continue

                    results = roll_multiple_dice(num_dice, num_sides)
                    print(f"Rolling {num_dice}d{num_sides}: {results} (Sum: {sum(results)})")

                except (ValueError, IndexError):
                    print("Invalid format. Please use 'roll XdY'. Example: 'roll 2d6'")
            else:
                print("Invalid 'roll' command. Please use 'roll' or 'roll XdY'.")
        else:
            print("Invalid command. Please use 'roll XdY' or 'back'.")

# --- RESTRUCTURED MAIN FUNCTION (THE MENU) ---
def main():
    print("Welcome to the Ultimate CLI Toolkit!")

    while True:
        print("\n--- Main Menu ---")
        print("1. Roll Dice")
        print("2. Play Shut the Box")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            handle_dice_rolling()
        elif choice == '2':
            play_shut_the_box()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
