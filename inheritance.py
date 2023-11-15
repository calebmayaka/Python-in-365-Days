"""Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
reduces code redundancy   """

#system that has managers and developers as employees
class employee:
    def __init__(default,firstname,lastname,pay):
        default.firstname = firstname
        default.lastname = lastname
        default.pay = pay
        default.fullname = firstname + " " + lastname

    #method to print full name

    def printfullname(default):
       return "{} {}" .format(default.firstname, default.lastname)
    
employee1  = employee("caleb","Mayaka", 380000)

print(employee1.fullname)
print(employee1.printfullname())

    
        

