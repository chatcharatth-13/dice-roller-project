import random
import itertools
import json
import os

def roll_single_die(num_sides=6):
    if not isinstance(num_sides, int) or num_sides < 1:
        raise ValueError("Number of sides must be a positive integer.")
    return random.randint(1, num_sides)

def roll_multiple_dice(num_dice, num_sides=6):
    if not isinstance(num_dice, int) or num_dice < 1:
        raise ValueError("Number of dice must be a positive integer.")
    return [roll_single_die(num_sides) for _ in range(num_dice)]

def save_game(tiles):
    with open('savegame.json', 'w') as f:
        json.dump({'open_tiles': tiles}, f)

def load_game():
    try:
        with open('savegame.json', 'r') as f:
            data = json.load(f)
            if 'open_tiles' in data:
                return data['open_tiles']
    except:
        pass
    return list(range(1, 13))

def is_move_possible(open_tiles, roll_sum):
    for i in range(1, len(open_tiles) + 1):
        for combo in itertools.combinations(open_tiles, i):
            if sum(combo) == roll_sum:
                return True
    return False