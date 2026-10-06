#from a file containing numbers separated bt comma, print the count of even numbers...
count = 0
with open ("numbers.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for value in nums:
        if (int(value)%2 == 0):
            count += 1
print(count)