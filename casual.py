def expense_tracker():
    expenses = []

    is_running = True
    while is_running:
        print("\n------Welcome to the Expense Tracker------")
        print("\nPlease choose an option: \n[1]Add Expense   [2]View Expenses    [3]Show Total   [4]Exit")

        try:
            choice = int(input("\nPlease choose an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
           bought = input("\nEnter What you Bought: ")
           cost = float(input("\nHow much it costs: "))
           expenses.append({
              "item": bought,
              "amount": cost
           })
           print("\nyour expenses succesfully tracked")

        elif choice == 2:
            for number, entry in enumerate(expenses, 1):
                print(f"{number}. {entry["item"]}: INR {entry["amount"]}")

        elif choice == 3:
            total = 0
            for entry in expenses:
                total = total + entry["amount"]
            print("\nyour total amount is:",total)

        elif choice == 4:
            is_running = False
            print("\nGoodbye!!")

        else:
            print("/n Plese choose a valid option")


expense_tracker()    