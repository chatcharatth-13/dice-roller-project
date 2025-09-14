import random

def roll_single_die(num_sides=6):
    """
    Rolls a single die with a specified number of sides.
    Defaults to a 6-sided die if num_sides is not provided.
    """
    if not isinstance(num_sides, int) or num_sides < 1:
        # นี่คือการจัดการกับกรณีขอบ (edge case) ที่ num_sides ไม่ถูกต้อง [8]
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

def main():
    print("Welcome to the Enhanced CLI Dice Roller!")
    print("Type 'roll XdY' to roll X dice with Y sides (e.g., 'roll 2d6' or 'roll 1d20').")
    print("Type 'roll' to roll a single 6-sided dice.")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("\nEnter command: ").lower().strip()

        if user_input == 'quit':
            print("Goodbye!")
            break
        elif user_input.startswith('roll'):
            parts = user_input.split()

            if len(parts) == 1: # Just 'roll'
                num_dice = 1
                num_sides = 6
                print(f"Rolling 1d6: {roll_single_die()}")
            elif len(parts) == 2 and 'd' in parts[1]: # 'roll XdY' - Corrected index from 13 to 1
                try:
                    dice_spec = parts[1].split('d') # Corrected index from 13 to 1
                    num_dice = int(dice_spec[0]) if dice_spec[0] else 1 # Allows 'd6' to mean '1d6'
                    num_sides = int(dice_spec[1]) # Corrected index from 13 to 1

                    # ตรวจสอบค่าที่ป้อนเข้ามา [8]
                    if num_dice < 1 or num_sides < 1:
                        print("Invalid input: Number of dice and sides must be positive. Example: 'roll 2d6'")
                        continue

                    results = roll_multiple_dice(num_dice, num_sides)
                    print(f"Rolling {num_dice}d{num_sides}: {results} (Sum: {sum(results)})")

                except ValueError as e:
                    # นี่คือการจัดการกับข้อผิดพลาดที่ผู้ใช้ป้อนข้อมูลที่ไม่ใช่ตัวเลข [8]
                    print(f"Invalid format or value: {e}. Please use 'roll XdY'. Example: 'roll 2d6'")
                except IndexError:
                    # Handle cases like 'roll d' or 'roll 2d' where split might not produce two parts
                    print("Invalid format. Please use 'roll XdY'. Example: 'roll 2d6'")
            else:
                print("Invalid 'roll' command. Please use 'roll', 'roll XdY'.")
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
