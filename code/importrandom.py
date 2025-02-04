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

#to select multiple random results, the choices is used with a value of k

value4 = random.choices(greetings, k=10)
print(value4)

#to define the probability of each of the greetings selected, we define weights

value5 = random.choices(greetings,weights=[10,10,2,2], k=10)
print(value5)

# range keyword - used to create number in a particular range

x = list(range(1,100))          #100 is exclusive

new_list = random.shuffle(x)        #shuffles the list
print(x)

