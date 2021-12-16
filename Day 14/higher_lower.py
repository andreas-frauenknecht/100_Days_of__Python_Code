from art import logo
from art import vs
from game_data import data
import os
cls = lambda: os.system('cls')
import random

def format_game_data(data):
    return

def get_random_compare():
    return random.choice(data)

def print_compare_info(data):
    name = data["name"]
    description = data["description"]
    country = data["country"]
    return f"{name}, a {description}, from {country}"

def check_guess(guess, compare_a, compare_b):
    compare_a_number = compare_a["follower_count"]
    compare_b_number = compare_b["follower_count"]
    if guess == "a" and compare_a_number > compare_b_number:
        return True
    elif guess == "b" and compare_b_number > compare_a_number:
        return True
    else:
        return False

def game():
    score = 0
    game_not_finished = True
    compare_a = get_random_compare()
    compare_b = get_random_compare()
    cls()
    print(logo)
    while game_not_finished:
        compare_a = compare_b
        while compare_b == compare_a:
            compare_b = get_random_compare()
        
        
        print(f"Compare A: {print_compare_info(compare_a)}")
        print(vs)
        print(f"Against B: {print_compare_info(compare_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_guess(guess, compare_a,compare_b)
        cls()
        print(logo)
        if is_correct:
            score+=1
            print(f"Thats right {guess} has more follower. Current score: {score}")
        else:
            game_not_finished = False
            print(f"Sorry, your guess {guess}, was wrong. Final score: {score}")

game()