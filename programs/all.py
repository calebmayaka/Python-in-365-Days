# # #uing the arbitratry arguements - used wneh you dont know how many parameters you are gonna pass to your function
# # def function1(*name):
# #     print("name is", name[0])

# # function1("caleb","mayaka","ombogo")

# # #arbitrary keywords

# # def function2(**names):
# #     print("his first name is", names["fname"])
    
# # function2(fname = "caleb", school = "eksa")

# # # assignemnt operators

# # ass1 = 100
# # ass1 = ass1 + 1
# # ass1 +-1
# # ass1 = ass1 * 1
# # ass1 /= 1

    #unction in birthday
# def birthday(name, yob):
#     print(f"Happy name is {name} your yob is {yob}")

# input_name = str(input("enter your name: "))
# input_yob = int(input("enter your year ob birth: "))
# birthday(input_name,input_yob)

    # book program using classes

class books:
    def __init__(self,name,author,yop,publisher,price):
        self.name = name
        self.author = author
        self.yob = yop
        self.publisher = publisher
        self.price = price
        
    def priceincrement(self):
        self.price = self.price * 1.1

author_input = str(input("enter your name: "))

book1 = books("python fundamentals", author_input ,"2024","callycalex technologies",13)

print(book1.name)

print(f"{book1.name} costs {book1.price}")

print("after price increment: ")

book1.priceincrement()
  
print(f"{book1.name}  by {book1.author} costs {book1.price} after price increment")