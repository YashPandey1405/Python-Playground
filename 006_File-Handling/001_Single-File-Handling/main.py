# Read From 'readFile.txt' File.....
readFile = open("readFile.txt")
data = readFile.read()
print(data)
readFile.close()

# Read From 'writeFile.txt' File.....
str = "Yash Pandey Is 21 Years Old..."
writeFile = open("writeFile.txt","w")
writeFile.write(str)
writeFile.close()

