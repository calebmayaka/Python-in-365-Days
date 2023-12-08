# classes are esentially like blueprints to create multipe stuff
# the class keyword is used to create a class
#suppose we want to create employee details. thisis agreat use case since each employee has specific attributes such as nams ,age, pay

class employee:                         #each employee that we create is as an instance of the class
    def __init__(self,firstname,lastname,pay):          # when methods are created inside a class, they receive a instance as a first arguement
        self.firstname = firstname                  #configure the instance variables
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + "." + lastname + "@gmail.com"
    
    #create a method to print full name
    def printfullname(self):
        return '{} {}' .format(self.firstname, self.lastname)
    

#creating the employees

employee1  = employee("caleb","Mayaka", 380000)
employee2 = employee("ombogo", "simwamu", 250000)

print(employee1.printfullname())
print(employee1.email)
print(employee2.email)