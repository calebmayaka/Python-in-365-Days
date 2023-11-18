# #blocks of code that cabb be called, they enhance the reusability and reduces redundancy

def function1(name, age):                #i have passed an argument or a parameter to the function, i can also pass multiple arguments
    print(f"my name is {name} and i am {age} years old")        #used a f string
    
function1(" caleb", 21)         #calling the function and giving the value that are required by the parameters/arguments

def addition(x,y):
    counter = 1
    addition_result = x + y
    while addition_result > 10:
        print("Greater than ten")
        counter = counter + 1
        if counter == 10:               #breaks when the counter reaches 10, break is very impontant to end loop statements
            break
    while addition_result < 10:
        print("less than ten")
        counter = counter + 1
        if counter == 10:               #breaks when the counter reaches 10, break is very impontant to end loop statements
            break
addition(5,6)
    
    #implemention using if else
def addition(x,y):
    counter = 1
    addition_result = x + y
    if addition_result > 10:
        while counter < 10 :
            print("Greater than ten")
            counter = counter + 1
                      
    elif addition_result < 10:
        while counter <10:
            print("less than ten")
        counter = counter + 1
addition(5,6)


# intergrated taking input from thw user
def addition(x,y):
    counter = 1
    addition_result = x + y
    if addition_result >= 10:
        while counter < 10 :
            print("Greater than ten")
            counter = counter + 1
                      
    elif addition_result < 10:
        while counter <10:
            print("less than ten")
            counter = counter + 1
        
x_input = int(input("enter the value of x: "))
y_input = int(input("enter the value of y: "))
    
addition(x_input,y_input)           #now is pass the input collected as values in the function on calling it
    
    