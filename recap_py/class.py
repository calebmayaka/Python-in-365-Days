# classes are blueprints for creating objects
# defined by the class keyword

class employee:
    def __init__(self,name,age,salary,position):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position
        self.email = f"{name}@gmail.com"
    def print_details(self):
        print(f"my name is {self.name} i am {self.age} years old, i am a {self.position} and i earn {self.salary} per month ")

    
employee1 = employee("caleb", 22, 450000, "Software Engineer")

print(employee1.age)

employee1.print_details()


class employee2:
    def __init__(self, name, proglang, location_posted):
        self.name = name
        self. proglang  = proglang
        self.location_posted = location_posted
    def print_info(self):
        print(f"my name is {self.name} i write {self.proglang} and i am based in {self.location_posted}")

name_input = str(input("enter your name: "))
lang_input = str(input("enter your programming language: "))
location_input = str(input("enter your location: "))

employee_2 = employee2(name_input, lang_input, location_input)

employee_2.print_info()