#used when you are not sure of how many arguments you are gonna pass to the function
# the * is used before the parameter/arguement.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("mayaka", "simwamu", "Mogaka")

# keyword arguments - defining specifically
def this_function(name1, name2, name3):
  print("name of the children are: " +name1 +name2 +name3)

  this_function(name1 = "caleb", name2 = "mayaka", name3 = "ombogo")