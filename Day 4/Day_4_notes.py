import random


random_integer = random.randint(1,10)
print(random_integer)

random_Float = random.random () * 5
print(random_Float)

toss = random.randint(0,1)
if toss == 1:
    print("Zahl")
else:
    print("Kopf")

states_of_america = ["Delaware","Pennsylvania","New Jersey","Georgia","Connecticut","Massachusetts"]
print(states_of_america[0])
a_state = states_of_america[2]
z_state = states_of_america[-1]
print(a_state+z_state)
states_of_america[1] = "Panncilvania"
print(states_of_america)
states_of_america.append("Maryland")
print(states_of_america)
states_of_america.extend(["South Carolina", "New Hampshire" , "Virginia"])
print(states_of_america)


# names_string = input("Give me everybody's names, separated by a comma. ")
names_string = "Andreas, Sascha, Pascal, Fabian"
names = names_string.split(", ")
name = names[random.randint(0,len(names)-1)]
print(f"{name} is going to pay the bill")
name = random.choice(names)
print(f"{name} is going to search the next bar")

#dirty_dozen = ["Erdbeere", "Spinat" , "Kohl", "Nektarine","Apfel" , "Trauben", "Pfirsich", "Kirschen" , "Birnen" , "Tomaten","Celeri","Kartoffen"]

fruits =["Erdbeere", "Nektarine","Apfel" , "Trauben", "Pfirsich", "Kirschen" , "Birnen"]
vegetables = ["Spinat" , "Kohl", "Tomaten","Celeri","Kartoffen"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
#print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
position = "23"
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column = int(position[0])
row = int(position[1])

map[row-1][column-1] = "X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


