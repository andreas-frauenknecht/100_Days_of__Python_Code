print("Welcome to the rollercoaster!")
height = 120#int(input("What is your hight in cm? "))
age = 18 #int(int(input("What is your age? ")))
#if else and comparater
if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        print(f"As you are {age} years old, you have to pay 5$")
    elif age <= 18:
        print(f"As you are 1{age} years old, you have to pay 7$")
    else:
        print(f"As you are {age} years old, you have to pay 12$")

else:
    print("Sorry you have to be higher than 120cm")
if height == 120:
    print("You are only 120 cm please ride with an adult.")
#Exercise with modular, if else and comparater
number = 21 #int(input("Please enter a random number: "))
odd = number%2
if odd == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")

# Exercise 3.2 BMI 2.0
#Code challange 2.2

# 🚨 Don't change the code below 👇
height = 1.85 # input("enter your height in m: ")
weight = 130 # input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = (int(float(weight)/ float(height)**2))
print(f"Your BMI is: {bmi}")
if bmi < 18.5:
    print("With a BMI under 18.5, you are underweight")
elif bmi <25:
    print("With a BMI between 18.5 and 25 you have a normal weight")
elif bmi <30:
    print("With a BMI between 25 and 30 you are overweight")
elif bmi <35:
    print("With a BMI between 30 and 35 you obese")
else:
    print("With a BMI over 35 you are clinically obese")

# Exercise 3.3 Leap year

year = 1200 #int(input("Which year do you want to check? "))

if year%4 == 0:
    if year%100 != 0:
        print("leap year")
    else:
        if year%400 == 0:
            print("Leap year")
        else:
            print("not a leap year")
else:
    print("not a leap year")


print("Welcome to the rollercoaster!")
height = 120#int(input("What is your hight in cm? "))
age = 45 #int(int(input("What is your age? ")))
bill = 0
#if else and comparater
if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        print(f"As you are {age} years old, you have to pay 5$")
        bill += 5
    elif age <= 18:
        print(f"As you are {age} years old, you have to pay 7$")
        bill += 7
    elif age >= 45 and age <= 55:
        print(f"As you are between 45 and 55 years old, you can ride for free")
    else:
        print(f"As you are {age} years old, you have to pay 12$")
        bill +=12
    wants_photo = "Y" #input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    
    print(f"You final bill is: ${bill}")

else:
    print("Sorry you have to be higher than 120cm")
if height == 120:
    print("You are only 120 cm please ride with an adult.")

    #Challange 3.4
    # 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = "M" # input("What size pizza do you want? S, M, or L ")
add_pepperoni = "Y" # input("Do you want pepperoni? Y or N ")
extra_cheese = "Y" # input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size == "S":
    bill += 15
    if add_pepperoni=="Y":
        bill += 2
elif size == "M":
    bill +=20
    if add_pepperoni=="Y":
        bill += 3
else:
    bill +=25
    if add_pepperoni=="Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

# Challange 3.5
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = "Donald Trump" #input("What is your name? \n")
name2 = "Angela Merkel" #input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
number_true = name1.count("t") + name1.count("r")+ name1.count("u") + name1.count("e") + name2.count("t") + name2.count("r")+ name2.count("u") + name2.count("e")
number_love = name1.count("l") + name1.count("o")+ name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o")+ name2.count("v") + name2.count("e")
love_percent = number_true*10+number_love

if love_percent < 10 or love_percent > 90:
    print(f"Your score is {love_percent}, you go together like coke and mentos.")
elif love_percent >= 40 and love_percent <= 50:
    print(f"Your score is {love_percent}, you are alright together.")
else:
    print(f"Your score is {love_percent}.")