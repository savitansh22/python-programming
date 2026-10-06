# create account class with 2 attributes - balance and account no.
#create methods for debot, credit, and printing the balance...

class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self, amount):
         if (amount>self.balance):
            print("insufficient balance")
         else:
            self.balance -= amount
            print("Rs. ", amount, "is debited from your account.")
            print("total balance is : Rs.",self.balance)

    def credit(self, amount):
        self.balance  += amount
        print("Rs. ", amount, "is credited to your account." )
        print("total balance is: Rs.",self.balance)

    def get_balance(self):
        return self.balance
    
acc1 = account(10000, "xxxxxxxxx")
print("Account no. : ", acc1.account_no)
print("your balance is: Rs.", acc1.balance)

print("choose debit or credit")
operation = input("write D for debit and C for credit: ").upper()

if (operation == "D"):
    acc1.debit(int(input("Enter amount to be debited: ")))
elif (operation == "C"):
    acc1.credit(int(input("Enter amount to be credited: ")))
else:
    print("you didn't choose any operation")
