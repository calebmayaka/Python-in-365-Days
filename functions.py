# A function is a block of code which only runs when it is called
#def is used to define a function
# functions form an aeasy way to organise code in parts

def function1():                        #defining the function
    print("this is a function")


function1()                             # this is calling the function


#arguments can be passed to the function by adding them inside the brackets, you can add s many as possible just separate them with commas


def greetings_app(firstname):
    print("Good morning " +firstname)

greetings_app("caleb")
greetings_app("mayaka")
greetings_app("ombogo")

#function that expectss two argurments
def greeting(studentname, class_):
    print("Hello " +studentname, "Your Class is " +class_)

greeting("caleb", "Cs")


# is youre not sure how many argurments are to be passed to the gunction nust use *

def my_function(*kids):
  print("The youngest child is " + kids[2])        # this uses an index

my_function("caleb", "ombogo", "mayaka")

# a list can be passed in a function
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



