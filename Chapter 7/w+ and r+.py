f = open("sample.txt", "r+")
data = f.write( "from basics")
f.close()

f =  open("sample.txt", "w+")
data = f.write("basics are very important")
f.close()