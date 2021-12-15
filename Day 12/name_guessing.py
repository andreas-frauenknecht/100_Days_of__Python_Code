import random
NUMBER_OF_GUESSES_HARD = 5
NUMBER_OF_GUESSES_EASY = 10

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
    


def set_difficulty():
    level = input("Choose a difiiculty. Type 'easy' or 'hard': ")
    if level == "hard":
        return NUMBER_OF_GUESSES_HARD
    else:
        return NUMBER_OF_GUESSES_EASY

number_to_guess = random.randint(1,100)
print(f"Debug: {number_to_guess}")

def game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    guesses_left = set_difficulty()
    guessed_number=0
    while guessed_number != number_to_guess:
        print(f"You have {guesses_left} attempts remaining to guess the number")
        guessed_number = int(input("Make a guess: "))
        guesses_left = check_answer(guessed_number, number_to_guess, guesses_left)
        if guesses_left == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guessed_number != number_to_guess:
            print("Guess again.")

game()