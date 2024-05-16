# functions
def function1(name, age):
    print(f"my name is {name} and i am {age} years old")


input_name = str(input("name: "))
input_age = int(input("age:"))

name_size = len(input_name)
# print(y)

if input_age > 115:
    print("wrong age")
else:
 if name_size >30:
    print("name too big")
 else:
    
   function1(input_name, input_age)

class caleb:
   def __innit__(self,name,age,id_number,position_employed,salary):
      self.name = name
      self.salary = salary
      self.age = age
      self.id_number = id_number
      self.position_employed = position_employed
      self.details = f"{name}, {age}, {id_number}, {position_employed}"

def apply_raise(self):
   self.salary = self.salary * 1.30


caleb1 = caleb()

print(caleb1.name)
   
      