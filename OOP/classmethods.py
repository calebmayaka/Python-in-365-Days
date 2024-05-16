class employee:
    raise_amount = 1.10 
    def __init__(self,name,age, pay):
        self.name = name
        self.age = age
        self.email = f"{name}@gmail.com"
        self.pay = pay

    def print_name(self):
        print(f"{self.name}")

# this method takes an instance of the class as the first arguement
    def set_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod            # class method decorator
    def set_raise_amount(cls,amount):
        cls.raise_amount =  amount
    




input_name = str(input("enter your name: "))
input_age = int(input("enter your age:" ))
input_pay = int(input("enter your pay:" ))

employee1 = employee(input_name, input_age, input_pay)

employee1.set_raise_amount(1.50)

print(employee1.raise_amount)

print(employee1.pay)
print(employee1.print_name())

