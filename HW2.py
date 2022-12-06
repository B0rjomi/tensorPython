import math
# task 1

def task_1(var_1, var_2):
    print(f"The result of addition =  {var_1 + var_2}")
    print(f"The result of subtraction = {var_1 - var_2}")
    print(f"The result of multiplication = {var_1 * var_2}")
    print(f"The result of division = {round(var_1 / var_2, 2)}")
    print(f"The result of exponentiation = {var_1 ** var_2}")
    print(f"The result of modulo division = {var_1 % var_2}")
    print(f"The result of integer division = {var_1 // var_2}")
    return "that's all the calculations"

# to run this function you need to uncomment 1 line of code from below
#print(task_1(float(input("Enter first number: ")), float(input("Enter second number: "))))

# task 2

def task_2(name):
    return(f"Hello, {name}")

# to run task_2 function you need to uncomment 1 line of code from below
#print(task_2(str(input("Enter your name: "))))

# task 3

def task_3(string):
    sub_string = ''
    sub_string = string[-2:]
    return sub_string[::-1]

# to run task_2 function you need to uncomment 1 line of code from below
#print(task_3(str(input("Enter some string: "))))

# task 4

def task_4(rad):
    return math.pi * rad**2

# to run task_2 function you need to uncomment 1 line of code from below
#print(task_4(int(input("Enter radius: "))))