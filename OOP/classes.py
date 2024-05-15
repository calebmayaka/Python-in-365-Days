class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.email = f"{name}@gmail.com"

    def print_name(self):
        print(f"{self.name}")

input_name = str(input("enter your name: "))
input_age = int(input("enter your age:" ))

employee1 = employee(input_name, input_age)


print(employee1.print_name())