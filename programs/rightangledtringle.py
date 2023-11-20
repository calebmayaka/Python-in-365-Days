x = int(input("Enter size of the adjacent: "))
y = int(input("Enter size of opposite: "))
hyp = int(input("Enter size of the hypotenuse: "))

xsq = x * x
ysq = y * y

sumofxandy = ysq + xsq


if sumofxandy == hyp*hyp:
    print("the triangle is a right angled triange ")
    
else:
    print("triangle is not a right angled triangle")