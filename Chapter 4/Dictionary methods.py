student = {
    "Name" : "Savitansh",
    "marks" : {
        "physics": 99,
        "chemistry": 98,
        "maths": 100
    }
}
print(student.keys())     #returns all the keys...
print(student.values())   #returns all the values.....
print(student.items())    #returns all (keys, values) pair as tuple...
print(student.get("marks"))   # returns the key accoridng to value....
student.update({"city": "srinagar"})
print(student)
