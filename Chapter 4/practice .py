#store following word meaning in a pyhton dictionary...
dict = {
    "table": ["a piece of furniture", "list of facts and figures"], 
    "cat": "a small animal"
}
print(dict)

#you are given a list of subjects for students. assume one classroom is required for 1 subject. how many classroom are needed be all students..
set = {"python", "c++", "python", "javascript"}
set2 = {"java", "python", "java", "c++", "c"}
print("no. of classroom needed:",len(set.union(set2)))

'''
write a program to enter marks of 3 subject from the user and store them in a dictionary. start with an empty dictioanry and 
add one by one. use subject name as key and marks as value..
'''
marks = {}
sub1 = int(input("physics: " ))
sub2 = int(input("chemistry:" ))
sub3 = int(input("maths:" ))

marks.update({"physics": sub1})
marks.update({"chemistry": sub2})
marks.update({"maths": sub3})

print(marks)

#figure out a way to store 9 and 9.0 as seperate values in the set.
set = {9,"9.0"}
print(set)

#or

set = {
    ("int",9),
    ("float",9.0)
}
print(set)