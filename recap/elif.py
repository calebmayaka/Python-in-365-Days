def score_input():
    student_score = int(input("Enter the student score: "))
    return student_score

# Get the student score
student_score = score_input()

# Check if the score is valid
while student_score > 100:
    print("Enter a value less than or equal to 100")
    student_score = score_input()

# Determine the student grade based on the score
if student_score > 80:
    print("Student grade is A")
elif student_score > 60:
    print("Student grade is B")
elif student_score > 40:
    print("Student grade is C")
elif student_score > 20:
    print("Student grade is D")
else:
    print("Student grade is E")
