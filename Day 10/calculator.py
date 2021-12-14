from art import logo

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": sub,
    "*": mul, 
    "/": div,
}
not_finished = True
reset = True
num1 = 0
num2 = 0


while not_finished:
    if reset:
        print(logo)
        num1 = float(input("What's the first number?: "))
        reset = False
    for key in operations:
        print(key)
    operation_symbol = input("Pick an operation (+,-,*,/): ")
    num2 = float(input("What's the next number?: "))
    function = operations[operation_symbol]
    result = function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'r' to restart or type a to abort: ")
    if choice == "r":
        reset = True
    elif choice == "y":
        num1 = result
    else:
        not_finished = False