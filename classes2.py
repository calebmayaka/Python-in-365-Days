# define the class
class employees:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.email = name + "." + "@eksa.com"

#define the details
employee1 = employees(21,"mayakaombogo")
employee2 = employees(24,"kemuntoruth")

# print
print(employee1.email)
print(employee2.name, employee2.age)
