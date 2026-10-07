#shorthand.py

from game_data import characters

def hero():
    return characters["player"]["health"]

def villain():
    return characters["enemy"]["health"]

def combat_active():
    return characters["player"]["health"] > 0 and characters["enemy"]["health"] > 0

def player_alive():
    return characters["player"]["health"] > 0

def enemy_alive():
    return characters["enemy"]["health"] > 0

def critical_success(dice):
    return dice == 20

def not_critical_success(dice):
    return dice != 20

def critical_fail(dice):
    return dice == 1

def not_critical_fail(dice):
    return dice != 1

def low_roll(dice):
    return 1 < dice < 5

def mid_low_roll(dice):
    return 5 <= dice < 10

def mid_roll(dice):
    return dice == 10

def mid_high_roll(dice):
    return 10 < dice <= 15

def high_roll(dice):
    return 15 < dice < 20

def one(number):
    return number == 1

def short_time(number):
    return 1 < number <= 5

def not_short_time(number):
    return number > 5

def awhile(number):
    return 5 < number <=15

def long_time(number):
    return number > 15

def small_attack():
    return characters["enemy"]["damage"]["light"]

def big_attack():
    return characters["enemy"]["damage"]["big"]

def huge_attack():
    return characters["enemy"]["damage"]["huge"]

def small_strike():
    return characters["player"]["damage"]["light"]

def big_strike():
    return characters["player"]["damage"]["big"]

def lucky_strike():
    return characters["player"]["damage"]["lucky"]