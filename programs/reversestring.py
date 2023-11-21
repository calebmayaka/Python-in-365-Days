
firstname = str(input("Enter your First Name: "))
lastname = str(input("Enter your Last Name "))

firstname_reversed = firstname[::-1]        # this method of reversing a string is called slicing.
lastname_reversed = lastname[::-1]


print(f"{firstname_reversed} {lastname_reversed}")