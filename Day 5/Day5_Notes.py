fruits = ["Apfel","Pfirsich","Birne"]
for fruit in fruits:
    print(fruit)
    print(fruit + "kuchen")

# 🚨 Don't change the code below 👇
student_heights = ["156","178","165","171","187"]#input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_hight = 0
total_number = 0

for student in student_heights:
    total_hight += int(student)
    total_number += 1

avarage = round(total_hight / total_number)

print(avarage)

# 🚨 Don't change the code below 👇
student_scores = ["15","33","21"] #input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
high_score = 0
for score in student_scores:
  if score > high_score:
    high_score = score

print(high_score)

for number in range (1,10):
    print(number)

for number in range (1,10,2):
    print(number)
total = 0
for number in range(1,101):
    total += number
print(total)
total = 0
for number in range(2,101,2):
    total += number
print(total)

for number in range(1,101):
    if number % 3 == 0:
        if number %5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number %5 == 0:
        print("Buzz")
    else:
        print(number)

