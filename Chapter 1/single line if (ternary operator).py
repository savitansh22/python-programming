# <var> = <val1> if <condition1> else <value2>
food = input("food: ")
eat = "yes" if food == "samosa" else "no"
print(eat)

# <stt1> if <condition> else <stt2>
food = input("food: ")
print("sweet") if food == "jalebi" or food == "rasgulla" else print("not sweet")
