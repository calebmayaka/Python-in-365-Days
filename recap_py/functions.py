# functions are defined by using the def keyword
# functions execute a block of text when called

def printName():
    print("caleb")

# calling the function

printName()

# arguements can be passed to functions

# function to ad two numbers

def addTwo(a,b):
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    sum = a + b
    
    print(sum)

addTwo()

def add_function(num1,num2):
    num1 = int(input("enter number 1:"))
    num2 = int(input("enter number 2:"))
    c = num1 + num2
    print(c)

add_function()



def add_function(num1,num2):
    c = num1 + num2
    print(c)

add_function(2,3)


def greetings_app(firstname):
    print("Good morning " +firstname)

greetings_app("caleb")
greetings_app("mayaka")
greetings_app("ombogo")

