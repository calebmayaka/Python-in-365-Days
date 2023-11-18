n = 5  # Assigning the value 5 to the variable 'n'

# Printing asterisks in an inverted pyramid
for i in range(n, 0, -1):  # Loop to iterate from n to 1 in decreasing order
    for j in range(i):  # Nested loop to print the asterisks in each row
        print('*', end='')  # Printing '*' (asterisk) without a newline
    print()  # Moving to the next line after printing the asterisks for a row
