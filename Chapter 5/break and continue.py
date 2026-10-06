#used to terminate the loop when encountered..
i = 0
while i <= 5:
    print(i)
    i += 1
    if (i==3):
        break
print("end of loop")

#terminates execution in the current iteration and continues execution of the loop with the next iteration.
i = 0
while i<=10:
    if (i == 5):
        i+=1
        continue  #skip..
    print (i)
    i += 1

