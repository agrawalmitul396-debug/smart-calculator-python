#Calc_Module.py

numOperations = 0

#Addition

def addition(a,b):
    global numOperation
    numOperation =+ 1
    return a+b

#Substraction

def substration(a,b):
    global numOperation
    numOperation =+ 1
    return a-b

#Multiplication

def multiplication(a,b):
    global numOperation
    numOperation =+ 1
    return a*b

#Division

def division(a,b):
    global numOperation
    if b == 0:
        return "Cannot Divide by Zero!"
    
    numOperation =+ 1
    return a/b

#Power with Default Argumen

def power(num,expo=2):
    global numOperation
    numOperation =+ 1
    return num ** expo

#Variable Length Argument

def sum_average(*number):
    global numOperation

    if len(number) == 0:
        return 0,0

    numOperation =+ 1

    total = sum(number)
    average = total/len(number)

    return total,average
