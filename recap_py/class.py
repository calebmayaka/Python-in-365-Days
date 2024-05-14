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