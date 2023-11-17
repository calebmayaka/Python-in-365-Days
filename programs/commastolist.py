# Accept input from the user
input_sequence = input("Enter a sequence of comma-separated numbers: ")

# Split the input sequence by commas and convert to a list of numbers
numbers_list = [int(num) for num in input_sequence.split(',')]

print("List of numbers:", numbers_list)

