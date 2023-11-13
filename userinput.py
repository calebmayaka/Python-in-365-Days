#for taking user input the input() function is used

x = input("enter your name:")    # pass the string you want to be displayed in prompt
print(x)

user_age = int(input("enter your age: "))           #the datatype is defined when you want an exact data type
user_name = str(input("enter your full name: "))    
user_age = str(user_age)            # typecasted this to avoid a concatenation error
print("your name is " + user_name ," and youre" + user_age ," years old") # commas added after every variable name

y = int(input("enter your marks: "))
y = str(y)
print("the marks that you score are " +y )


