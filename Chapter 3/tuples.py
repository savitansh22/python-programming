# A built-in Data type that lets us create immutable sequences of values.
tup = (2,3,1,4)
print(tup)
print(tup[1])
print(tup[0])
#tup[1] = 5   not allowed because it is immutable.
print(tup.index(1))
print(tup.count(2))
