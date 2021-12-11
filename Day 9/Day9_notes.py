programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}
print(programming_dictionary)

#get stuff
print(programming_dictionary["Bug"])

#add stuff
programming_dictionary["Fix"] = "The action to remove a bug"
print(programming_dictionary)
#create one
empty_dictionary = {}
print(empty_dictionary)

#edit
programming_dictionary["Bug"] = "Program works fine"
print(programming_dictionary)

#loop
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#wipe it
programming_dictionary = {}
print(programming_dictionary)

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)


#Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# not so useful
list_list = ["A", "B", ["C","D"]]

enhanced_travel_log = {
    "France": {"Cities visited":["Paris", "Lille", "Dijon"], "total_visits":12},
    "Germany": {"Football_stadiums": ["Berlin", "Hamburg", "Stuttgart"], "total_visits":140},
}

travel_list = [
    {
        "country":"France", 
        "cities visited":["Paris", "Lille", "Dijon"], 
        "total_visits":12
    },
    {
        "country":"Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits":140
    },
]

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country,visits,cities):
    new_entry = {"country":country,"visits":visits,"cities":cities}
    travel_log.append(new_entry)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


