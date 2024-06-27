
# # Using *args
# def add(*args):
#     sum = 0
#     for each in args:
#         sum += each
#     return sum

# def subtract(*args):
#     difference = 0
#     for each in args:
#         difference -= each
#     return difference

# def multiply(*args):
#     multiply = 1
#     for each in args:
#         multiply *= each
#     return multiply


# 1. Writing a calculator program using functions:
# In this case the parameters were called "x" and "y", but any other letter or words can work with this.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error, division by zero"
    return x / y

def get_user_input():
    operation = input("Operation to perform (+, -, *, /): ")
    if operation not in ["+", "-", "*", "/"]:
        print("Operation not recognised")
        return None, None, None
    
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    return operation, x, y

def calculator_functions ():
    while True:
        operation, num1, num2 = get_user_input()
        result = 0
        if operation is None:
            return 0
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)


        print(f"The result is: {result}")

        next_calculation = input("Do you want to perform another calculation ( yes / no): ")
        if next_calculation.lower() != "yes":
            break

calculator_functions()