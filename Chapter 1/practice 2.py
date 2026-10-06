#write a program to grade students based on marks.

marks = int(input("enter your marks: "))
if (marks >= 90):
    grade = "A"
elif (80 >= marks > 70):
    garde = "B"
elif (70 >= marks > 60):
    grade = "C"
elif (marks <= 60):
    grade = "D" 
print("your grade is:", grade)