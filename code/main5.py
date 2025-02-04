"""print("good evening caleb")
list1 = ["caleb", "mayaka", "ombogo"]
print(list1)
print(type(list1))
list1.append("simwamu") #appending method - adds an item at the end of the list
print(list1)
list1.clear()
print(list1)
print(list1)
print(list1)  """ # this is a docstring - fancy name for multiline comments

caleblist = list(("Mayaka","caleb","ombogo")) # list constructor
print(caleblist)
print(caleblist[0:2]) #printing list items by specifying the range
print(caleblist[2:0])
# del caleblist - this will delete the list
# caleblist.remove("caleb")  - removes an item from a specific index
print(caleblist)

print(caleblist[-2]) #negative indexing - prints from the back forward

if "caeb" in caleblist:
    print("caleb is present in the list") # checks whether an item is in the list
else:
    print("caleb is not present in the list") # this also shows the use of a if  and else statements

secondlist = [10,20,30,40]
print(secondlist)
secondlist[0:3] = [100,110,120]  # this changes values in a specific range
print(secondlist)

secondlist.insert(1,1000)  #inserts/ replaces an item at a particular index
print(secondlist)

secondlist.pop(1)
print(secondlist)       #pop method deletes an item in a specified index

for x in secondlist:
    print(x)            #loops through the list and prints all the items in the list. 

