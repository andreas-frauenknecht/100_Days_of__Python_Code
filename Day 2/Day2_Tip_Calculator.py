print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
how_many_person = int(input("How many people to split the bill? "))
pay = round((bill + (bill/100*percentage))/how_many_person,2)
pay_with_always_two_numbers_after_decimalpoint = "{:.2f}".format(pay)
print(f"Each person should pay: ${pay_with_always_two_numbers_after_decimalpoint}")