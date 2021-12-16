MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_available_coffee():
    available_coffee = ""
    for coffee in MENU:
        available = True
        ingredients = MENU[coffee]["ingredients"]
        for ingredient in ingredients:
            if resources[ingredient] <= MENU[coffee][ingredients][ingredient]:
                available = False
        if available == True:
            available_coffee += coffee + " "
    return available_coffee


balance = 0.0
coffee_available = ""
while True:
    print("Welcome to the coffee-maker-2000. Please select your action:")
    print("If you want a coffee type: 'espresso', 'latte', 'cappuccino'")
    print("if you want to put in money press: '1F', '50R', '20R' or '5R")
    print(f"Your balance is: {balance} and following coffee are available for you: {check_available_coffee()}")
#Print status line and wait for user to do something
    choice = input("Your choice? : ")
#The status line should contain the available coffee drinks
#  and the current account of money entered

#user does something

#check what the user has done

#if he has entered money add it to the value

#if he has refunded the money give it back

#if he has selected coffee makeing check if rescource and money are ok
# if not enough money do nothing and print an error message
# if rescource not enought print error message do nothing
# all good then print coffee making message and reduce the balance by the price,
# and give the money back that is over and set balance to 0
