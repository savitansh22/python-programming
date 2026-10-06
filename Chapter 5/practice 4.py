# print numbers from 1 to 10..
for i in range(1,101):
    print(i)

#print number from 100 to 1..
for i in range(100,0, -1):
    print(i)


#print the multiplication table of a number n...
n = int(input("enter a numberr: "))
for i in range (1,11):
    print(f"{n} x {i} = {n*i}")