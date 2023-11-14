def function(name, school):
    print("My name is " + name + ", and my school is " + school)

# Get input outside the function
name = str(input("Enter your name: "))
school = str(input("Enter your school: "))          #use the same variable names in the parameters/arguements and the variable names

# Call the function with the input values
function(name, school)                          #is a function expects like two values passed to it and you pass only one it will return an erro

