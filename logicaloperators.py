#used to combine conditional statements
x = 250
z = 100
w = 50

if x > z and x > w:
    print("x is greate than both z and w")

if x > z or x > w:
    print("x is greate than both z and w")

if not x > z or x > w:
    print("x is greate than both z and w")
else:
    print("not any of the two")


