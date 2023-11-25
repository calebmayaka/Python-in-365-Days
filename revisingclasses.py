
class employee:
    age = 0
    number_of_students = 0
    def __init__(self,name,town,dob,university):
        self.name = name
        self.town = town
        self.dob = dob
        self.university = university
        
        self.twitter = "twitter.com/ombogomayaka"
        
    number_of_students += 1
    added = number_of_students
        
    def age (self):
        employee.age = 2023 - self.dob
        return employee.age
    
input_name = str(input("Enter your name: "))
input_town = str(input("Enter your town: "))
input_dob = int(input("Enter your dob: "))
input_uni = str(input("Enter your university: "))


employee1 = employee(input_name,input_town,input_dob,input_uni)

print(f"the name of the employee is {employee1.name} the come from {employee1.town} they are aged {employee1.age()} and they studied in {employee1.university}")


print(employee.number_of_students)