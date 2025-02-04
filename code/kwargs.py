#this is another python function parameter passing type
#stands for keyword arguements and uses.
# the function receives a dictionary of arguments

def myfunction(**kid):                          #essentially kwargs deals with dictionary
    print("this kid is called" +kid["lname"])
    
myfunction(fname = "caleb", lname = " mayaka")