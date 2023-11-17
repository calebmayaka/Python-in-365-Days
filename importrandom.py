import random                   #importing the random module which contains the functions necessary for generating and working with random numbers

value = random.random()          #calling the random function, it prints a random number between 1 and  by default              
print(value)

#to get random integers

value2 = random.randint(1, 8)
print(value2)

# if we want to choose a random greeting from a list of greeitngs

greetings = ["hello", "Morning", "habari","Ssup"]

value3 = random.choice(greetings)

print(f"{value3}, caleb")

