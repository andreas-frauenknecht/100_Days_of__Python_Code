from art import logo
import random

import os
cls = lambda: os.system('cls')

def deal_card():
    '''Returns a random card from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(hand):
    '''Take a list of cards and return the socre of the cards. Returns 0 if Blackjack'''
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(user_score, computer_score):
    '''Checks if'''
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You loose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    user = []
    dealer = []

    for _ in range(2):
        user.append(deal_card())
        dealer.append(deal_card())

    game_running = True

    while game_running:
        cls()
        print(logo)
        user_score = calculate_score(user)
        dealer_score = calculate_score(dealer)


        print(f"   Your cards: {user}, current scorce: {user_score}")
        print(f"   Dealer cards: {dealer[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_running = False
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user.append(deal_card())

            else:
                game_running = False

    while dealer_score != 0 and dealer_score < 17:
        dealer.append(deal_card())
        dealer_score = calculate_score(dealer)
    cls()
    print(logo)
    print(f"   Your cards: {user}, end scorce: {user_score}")
    print(f"   Dealer cards: {dealer} end score: {dealer_score}")
    print(compare(user_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    cls()
    play_game()