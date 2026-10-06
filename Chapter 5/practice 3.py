#print the elements of the following list using for loop...
l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in l:
    print(i)

# search for a number x in this tuplw using for loop..
l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(l)
x = int(input("enter a number: "))

idx = 0
for i in l:
    if (i == x):
        print("number is found at idx:", idx)
    idx += 1
