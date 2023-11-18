# Arbitrary Positional Arguments (args) in full
"""The *args parameter in a function definition allows you to pass a variable 
number of positional arguments. When a function parameter is 
preceded by an asterisk (*), it collects all the positional arguments into a tuple within the function."""

# def function_1(*kids):
#     print("the youngest kid is ", kids[2])

# function_1("caleb", "Mayaka", "Ombogo")


def my_function2(*kids):                
    for kid in kids:                        #using kid and kids to differentiate between  a single item and a collection
        print(kid)

my_function2("caleb", "mayaka", "ombogo")