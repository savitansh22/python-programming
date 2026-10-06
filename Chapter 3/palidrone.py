#write a program to check if a list contains a palindrone of elements.
list = []
list.append(input("a:"))
list.append(input("b:"))
list.append(input("c:"))
list.append(input("d:"))

list2 = list.copy()
list2.reverse()
if (list == list2):
    print("palindrone")
else:
    print("not palindrone")