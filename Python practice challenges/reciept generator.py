def reciept_generator():
    total = 0
    print("enter prices of items and seperate them with a space")
    prices = input() 
    price = prices.split()
    for x in price:
        total += float(x)
    return total

reciept = reciept_generator()
print("total price of the items is: ", reciept)
