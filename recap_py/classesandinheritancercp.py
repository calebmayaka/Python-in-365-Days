# classes act like blueprints for creating objects
# they use the class keyword

class employee:   # class definition
    def __init__(self, name, age):  # init method
        self.name  = name
        self.age  = age
    def print_name_age(self):
        print(f"my name is {self.name } and i am {self.age} years old")

input_name = str(input("enter your name: "))
input_age  = int(input("enter your age: "))

employee1 = employee(input_name, input_age)

print(employee1.name)

employee1.print_name_age()

class  developer(employee):
    def __init__(self,name,age,prog_language):
            super().__init__(name,age)
            self.prog_language = prog_language
    def devstuff(self):
         print(f"this developer is called {self.name} and he uses {self.prog_language}") 
        
input_proglang = str(input("enter your programming language: "))
developer1 = developer(input_name, input_age, input_proglang)

developer1.devstuff()