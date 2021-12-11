import os
from art import logo

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def find_highest_bidder(bidder_list):
    highest_bid = 0
    winner = ""
    for bidder in bidder_list:
        bid_amount = bidder_list[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print(logo)
conti = "yes"
bidder_list = {}
while conti == "yes":
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    bidder_list[name] = bid
    conti = input("Is there another bidder? (yes/no): ")
    cls()
find_highest_bidder(bidder_list=bidder_list)



