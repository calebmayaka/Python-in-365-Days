# define a class

class employees:                                               #defines the employee class
    def __init__(default, firstname, lastname, salary,age):     #this is a function that hold tha variables of the class. - class attributes
        default.lastname = lastname                             #here the variables are initialized
        default.salary = salary
        default.age = age
        default.fullname = firstname + " " + lastname

employee1 = employees("Caleb", "Mayaka", 250000, 21)              #data is passed to on instance of the class

print("my name is", employee1.fullname, "and i am ", employee1.age, "years old and i get paid", employee1.salary)                                          #printing of the employee 1 details
