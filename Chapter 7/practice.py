#create a new file "practice.txt" using python. Add the following data in it...
with open("practice.txt", "w") as f:
    f.write("Hi, Everyone \n we are learning File I/O \n Using java.")

# write a function that replace all occurences of "java" with "python" in above file..
with open("practice.txt", "r") as f:
    data = f.read()    
print(data)
new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

#search if the word "learning" exists in the file or not..
find = input("enter the word: ")
with open("practice.txt") as f:
    data = f.read()
    if (data.find(find)!= -1):
        print("Found")
    else:
        print("not Found")