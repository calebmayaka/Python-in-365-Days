# Accept input from the user for the filename
filename = input("Enter a filename: ")

# Find the position of the last dot in the filename
last_dot_index = filename.rfind('.')

if last_dot_index != -1:
    # Extract and print the file extension
    file_extension = filename[last_dot_index + 1:]
    print("The extension of the file is:", file_extension)
else:
    print("No extension found in the filename.")
