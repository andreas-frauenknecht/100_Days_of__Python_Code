# Functions
def greet(name):
    print(f"Hello {name}")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet("Mr. Smith")
name = "Mrs. Bolston"
greet(name)

for i in range(15):
    greet(i)

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Mr. Smith", "Winterthur")
greet_with(location="Winterthur",name="Mr. Smith")

# excercise
#Write your code below this line ๐

import math

def paint_calc(height, width, cover):
    total_sqm = height * width
    total_cans = math.ceil(total_sqm / coverage)
    print(f"You'll need {total_cans} can(s) of paint.")

#Write your code above this line ๐
# Define a function called paint_calc() so that the code below works.   

# ๐จ Don't change the code below ๐
test_h = 9 #int(input("Height of wall: "))
test_w = 3 #int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# exercise

#Write your code below this line ๐
def prime_checker(number):
    prime =""
    for i in range(2,number):
        if number % i == 0:
            prime = " not"
    print(f"It's{prime} a prime number")


#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)