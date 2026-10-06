'''num = int(input("enter a number: "))
i = 1
fact = 1
while i <= num:
    fact *= i
    i += 1
print(fact)'''

#better way to find factorial is by using recursion....

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)


num = int(input("enter a number: "))
fact = factorial(num)
print(fact)


def factorial_trailing_zero(fact):
    count = 0
    while fact%10 == 0:
        count += 1
        fact = fact /10
    return count

trailing_zeros = factorial_trailing_zero(fact)
print(trailing_zeros)