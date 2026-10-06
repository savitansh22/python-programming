# All classes have a function called __intit__(), which is always executed when the object is being initiated...
class student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database....")

    def welcome(self):
        print("welcome", self.name)

s1 = student("karan", 97)
s1.welcome()
print(s1.name, s1.marks)

s2 = student("arjun", 85)
s2.welcome()
print(s2.name, s2.marks)