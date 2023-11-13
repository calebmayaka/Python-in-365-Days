#enclosed in either single or double quotation marks
#python does not have a character data type hence characters are considered a string with length of 1

x = "caleb"
print(x)
print(type(x))

#square brackets can be used to access the characters in a sting
#the index starts at 0
print(x[2])
print(x[1:3]) #specifies a range
print(x[0:5])

#other functions and methods
        #strip - removes whitespaces at the beginning and end
y = "caleb "
print(y)
y.strip()
print(y)
        #len - returns the name of a string
print(len(x))

        #lower-- stings to lower case
print(y.lower())

        #upper-- stings to upper case
print(y.upper())