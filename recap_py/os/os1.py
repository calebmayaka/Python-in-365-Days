import os
# print(dir(os))  #prints all the methods that aer available to the user

print(os.getcwd())

# os.chdir("/users/caleb")  # changes the working directory

print(os.listdir())

# os.mkdir("osdir__")
# os.makedirs("osdir1/dir1")

os.rmdir("osdir")
# os.removedirs("osdir1/dir1")