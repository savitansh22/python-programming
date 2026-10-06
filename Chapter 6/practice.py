#write a function to print the length of a list..
while True:
    list1 = []
    def length(list):
        print(list)
        print(len(list))

        print("type the item you want to add, and type done when finished...")

    while True:
        inp = (input("enter item: "))
        if (inp == "done"):
            break
        list1.append(inp)

    length(list1)
