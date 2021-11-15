#Data Types

#String
print("Hello"[4])
#This does not add the 2 numbers together
print("123"+"456")

#Integer
print (123+456)
print(123_456_789)
#Int can be as big as you wish
a=123432942304802384023840912384092384324198735902347895723984572438523498508912347230984719023847234123423142314123423423412344123412412345345235324534253245234532453245234532458237140972398712389749081237487123498712364891236487916234897612389461238994308759034875902348750234759072349058723490857902348509234875920348572390458732490587234905873249085702934759023487590234875903247593425233333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
a=a**9
print(a)
#Hex
a=-0x260
print(a)

#float

f1=3.14159
f2=10/3
f3=10//3 # Modula
f4=f2*3
f5=f2*f1
print(f"{f1},{f2},{f3},{f4},{f5}")

# Boolean
b1 = True
b2 = True
b3 = False
b4 = False 
b5=b1+b2+b3
print(b5)

#Type conversions

#num_char = len(input("What is your name: "))
num_char = "Andreas"
new_num_char = str(num_char)
print ("Your name has "+new_num_char+" characters")

a=123
print(type(a))
a = str(a)
print(type(a))


#Day 2.1 Data Types Excercise
print ("For an example number 56 the program calculates 11")
two_digit_number = "56"
print(int(two_digit_number[0])+int(two_digit_number[1]))

#Math
print(2+2)
print(type(2+2))
print(2-9)
print(type(2-9))
print(2*4)
print(type(2*4))
print(6/2)
print(type(6/2))
print(3**3)
print(type(3**3))

#PEMDAS
# ()
# **
# * /
# + -
# left before right

#short example to get 4 with only +-*/ used exatly one time and only 3 as number 4 time
print (((3-3)+3)/3+3)

#Code challange 2.2

# 🚨 Don't change the code below 👇
height = 1.85 # input("enter your height in m: ")
weight = 96 # input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print("BMI:")
print(int(float(weight)/ float(height)**2))

# How to deal with float and rounding

#Float rounded to full decimal
print(round(8 / 3))
#Float rounded to the place after decimal
print(round(8/3,2))
#just take the decimal part of the division --> gives int
print(8 // 3)
result = 4/2
result /= 2
print(result)
result += 1
result *=5
print (result)

score = 0
len = 1.8
isWinning = True

# f string
print(f"your score is {score}, with length {len} and your winning is {isWinning}")

# Code challenge
# 🚨 Don't change the code below 👇
age = 67 #input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)
days = (90*365) - (age_as_int*365)
weeks = (90*52) - (age_as_int*52)
months = (90*12) - (age_as_int*12)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")