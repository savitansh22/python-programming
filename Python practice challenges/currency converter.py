with open ('currency_data.txt') as f:
    lines = f.readlines()

curr_dict = {}
for line in lines:
    extract = line.split("\t")
    curr_dict[extract[0]] = extract[1]

amount = int(input("Enter amount to be exchanged: \n"))
print("Enter the name of currency, you want to convert this amount. Available options are: \n")
[print(item) for item in curr_dict]
currency = input("Enter one of these values: \n ")
print(f"INR {amount} = {amount*float(curr_dict[currency])}{currency}")