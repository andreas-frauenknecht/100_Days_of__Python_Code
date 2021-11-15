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

year = int(input("Which year do you want to check? "))

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