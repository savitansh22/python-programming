#write a function to print the elements of a list in a single line...
cities = ["delhi", "dehradun", "karanprayag", "srinagar"]
def items(list):
    for item in list:
        print(item, end= " ")

items(cities)