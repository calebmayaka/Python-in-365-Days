#lists are one of the four different types of collection data typesin python
"""lists use square brackets
    they are indexed 
    they are ordered and changaeble
        a list can contain items from multiple data types"""

this_list = ["caleb", 2]

print(this_list)        #prints the list
print(this_list[1])     #printing the first object in the list -index starts at 0

this_list[0] = "mayaka" #the index can be used to change the values of the list
print(this_list[0])

# the list construtor - list()
this_constructorlist = list(("mayaka", "ombogo", "caleb", "21"))

print(this_constructorlist[2])

