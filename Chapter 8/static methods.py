# methods that don't use the self parameter...
class student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database....")

    @staticmethod
    def hello():
        print("hello")

    def welcome(self):
        print("welcome", self.name)

s1 = student("karan", 97)
s1.hello()
s1.welcome()
print(s1.name, s1.marks)

s2 = student("arjun", 85)
s2.welcome()
print(s2.name, s2.marks)