def add_function():                         #when you want to take input in a function you dont give parameters/ arguements to it
    num1 = int(input("enter number 1:"))
    num2 = int(input("enter number 2:"))
    c = num1 + num2
    print(c)

add_function()

# return value - this keyword deliveres the output but does not print it

def function2():
    number1 = int(input("enter number 1: "))
    number2 = int(input("enter number 2: "))

    a = number1 + number2
    return a

A = function2()                   #after using the return keyword, it is impontant to assign the function to a variable when calling it
print(A)

#you can return multiple values at the same time

def function2():
    number1 = int(input("enter number 1: "))
    number2 = int(input("enter number 2: "))

    a = number1 + number2
    b = number1 - number2
    return a,b

A,B = function2()                   #after using the return keyword, it is impontant to assign the function to a variable when calling it
print(A,B)

