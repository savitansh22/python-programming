# write a program to find the sum of first n numbers. (using while)
n = int(input("enter your number: "))
sum = 0
i=1
while i <= n:
     sum += i
     i += 1
print("sum:", sum )

# same using for loop...
n = int(input("enter your number: "))
sum = 0
for i in range(1, n+1):
     sum += i
print("sum:", sum)

#write a program to find the factorial of first n numbers. (using for)
n = int(input("enter your number: "))
fac = 1
for i in range(1,n+1):
     fac *= i
     i += 1
print("factorial:", fac)

#same using while loop...
n = int(input("enter your number: "))
fac = 1
i = 1
while i<=n:
     fac *= i
     i += 1
print("factorial:", fac)