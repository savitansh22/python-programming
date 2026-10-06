# write a function to find in which line of the file does the word "learning" occur first...
find = input("enter a word: ")

def find_line():
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (find in data):
                print(line_no)
                return
            line_no += 1
    return -1
find_line()