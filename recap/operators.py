#there are multiple types of operators 

# arithmetic operators
x = 10
y = 20

addition = x + y 
subtraction = x - y
division  = x / y
multiplication = x * y
floordivision = y // x*y
exponentiation = x ** y
modulus = y // x
print(addition,subtraction,division,multiplication,modulus,floordivision,exponentiation)

# comparison operators

"""
== (Equal to)
!= (Not equal to)
< (Less than)
> (Greater than)
<= (Less than or equal to)
>= (Greater than or equal to)

"""
while x == y:
    print("they are equal")
else:
    print("they arent equal")
    
# Logical Operators

    """
and (Logical AND)
or (Logical OR)
not (Logical NOT)
    
    """
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# assignment operators
"""
= (Assignment)
+= (Add and assign)
-= (Subtract and assign)
*= (Multiply and assign)
/= (Divide and assign)
%= (Modulus and assign)
**= (Exponentiate and assign)
//= (Floor divide and assign)
    """
    
x = 5
x += 1      #increments
print(x)