            #functions that are defined inside a class in python are called methods
            #methods are sort of functions associated with a particular object
            #for example in the random module has a number of functions such as random,shuffle,sample
# methods, by definition, are functions that are associated with classes. They are accessed via instances or the class itself and are designed to operate on the attributes and data within those instances or the class.

# Defining a simple class


class Dog:                          #creating a class
    def __init__(self, name, age):  #initializes class constituents
        self.name = name            
        self.age = age

    def bark(self):                 #creating an instance method bark
        return "Woof!"

# Creating instances (objects) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing attributes and calling methods of objects for both the variables and methods           
print(dog1.name)  # Output: Buddy
print(dog2.age)   # Output: 5
print(dog1.bark())  # Output: Woof!
