#write a function to find the factorial of n...
while True:
    n = int(input("input a number: "))
    def cal_fact(num):
        fac = 1
        for i in range(1, n+1):
            fac *= i
        print(fac)
    cal_fact(n)
