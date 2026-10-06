#print the multiplication table of a number n.
n = int(input("enter your number: "))
i = 1
while i<=10:
    print(i*n)
    i+=1

#print the element of following list using a loop. [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 1
while i<=10:
    print(i**2)
    i+=1

#search for a number x in this type tuple using loop. (1, 4, 9, 16, 25, 36, 49, 64, 81, 100).
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(nums)

x = int(input("enter a number: "))

i = 0
while i < len(nums):
    if (nums[i] == x):
        print("NUM FOUND AT INDEX: ",(i))
    i += 1
    