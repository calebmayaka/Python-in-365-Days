#used when you are not sure of how many arguments you are gonna pass to the function
# the * is used before the parameter/arguement.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("mayaka", "simwamu", "Mogaka")
