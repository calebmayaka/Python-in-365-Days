# this is a function that is used to generate number in a range
import random           #import random module 

for i in range(1,100):          #loops and prints the number in order
    print(i)

# here we store the number in a list using a list constructor
x = list(range(1,100))      #created a list of number between 1 and 100

print(x)            #prints out the list

# i can randomize the number in the list using the random module

randomized = random.shuffle(x)          #using the shuffle method

print(x)