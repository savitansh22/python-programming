#create student class that takes name and marks of 3 subjects as argument in constructor. them create a method to print the average...
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

n = input("ENTER YOUR NAME: ")
m1 = int(input("MARKS IN PHYSICS: "))
m2 = int(input("MARKS IN CHEMISTRY: "))
m3 = int(input("MARKS IN MATHS: "))
    
avg = (m1 + m2 + m3)/3

s1 = student(n, avg )
print("hi", s1.name, "your average score is:", s1.marks)