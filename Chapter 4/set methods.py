set = set()
set.add(1)   #adds an element..
set.add(2)
set.add(2)
set.add(3)
print(set)

set.remove(2)   #removes the element..
print(set)

set.clear()   #empties the set..
print(set)

set = {1,2,3,4}
set.pop()    # removes a random value..
print(set)

set2 = {3,4,5,7,8}
print(set.union(set2))   # combines both set and returns new...

print(set.intersection(set2))    # combines common values and returns new....