# <var> = ( "false_value", "true_value" ) [condition]
age = int(input("age: "))
vote = ("no", "yes") [age>=18]
print(vote)

#second example:
sal = float(input("salary: "))
tax = sal*(.1, .2) [sal>=500000]
print(tax)