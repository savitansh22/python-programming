def evens(numbers):
    even_list = []
    for num in numbers:
        if (num % 2 == 0):
            even_list.append(num)
    return even_list

my_list = [1,2,3,4,5,6,7,8,9,10]

result = evens(my_list)
print(result)

