#Functions
def my_function():
    result = 3*2
    return result

print(my_function())

def format_name(f_name,l_name):
    """Take a first and last name and format it to 
    return the title case version of the name"""
    if (f_name == "" or l_name == ""):
        return "Wrong input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("aNdReAs" , "FRAUENKNECHT")
#formated_string = format_name(input("Enter your first name: ") , input("Enter your last name: "))
print(formated_string)

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month-1]
        
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)