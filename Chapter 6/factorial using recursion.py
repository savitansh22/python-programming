n = int(input("Enter a number: "))

def fact(fac):
    if (fac == 0 or fac==1):
        return 1
    else:
        return fact(fac-1)*fac
    
print(fact(n))
