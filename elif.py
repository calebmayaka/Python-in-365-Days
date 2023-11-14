student_age = int(input("enter student age:"))
if student_age < 10:
    print("student is less than ten years")
elif student_age >= 30:                             # the 30 year elif statement is put first in order to stop endless true nature of the 20 year elif  
    print("student is older than 30 years")
elif student_age >=20:
    print("student is greater than 20 years")
else:
    print("dude are you an alien")