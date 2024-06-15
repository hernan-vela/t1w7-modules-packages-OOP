def add(*args):
    sum = 0
    for each in args:
        sum += each
    return sum

def subtract(*args):
    difference = 0
    for each in args:
        difference -= each
    return difference

def multiply(*args):
    multiply = 1
    for each in args:
        multiply *= each
    return multiply


print(multiply(5, 6, 1, 4))
