import os
# print(dir(os))  #prints all the methods that aer available to the user

print(os.getcwd())

# os.chdir("/users/caleb")  # changes the working directory

# print(os.listdir())

# os.mkdir("osdir__")
# os.makedirs("osdir1/dir1")

# os.rmdir("osdir") # will not remove intermediate directories

# os.removedirs("osdir1/dir1")  # will remove all in the directory

os.walk("") # lists 3 value tuple of path, dir name and filenames

# rename

# os.rename("test.txt" , "new.txt")

print(os.stat("datatypes.py"))

# environment variables

print(os.environ.get("HOME"))