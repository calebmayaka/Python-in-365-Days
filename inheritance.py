# System that has managers and developers as employees
class Employee:
    raise_new = 1.04  # Note: I changed the class name to follow Python naming conventions

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.fullname = firstname + " " + lastname

    def printfullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    def apply_raise(self):
        self.pay = int(self.raise_new * self.pay)

class Developer(Employee):  # Inheriting from Employee
    def __init__(self, firstname, lastname, pay, prog_lang):
        super().__init__(firstname, lastname, pay)
        self.prog_lang = prog_lang

# Instances of Developer class
employee1 = Developer("Caleb", "Mayaka", 380000, "Python")
employee2 = Developer("Ombogo", "Mayaka", 380000, "JavaScript")

# Print statements outside the class
print(employee1.firstname, employee1.lastname)
