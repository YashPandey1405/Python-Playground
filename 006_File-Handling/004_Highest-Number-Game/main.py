import random

with open("file.txt", "w") as file:
    pass 
 
def WriteInFile(num):
    print(f"Updated Number Is : {num}")
    with open("file.txt", "w") as file:
        file.write(str(num))

def HighestNumberGame():
    random_int = int(random.random() * 100)
    readFile = open("file.txt")
    num = readFile.read()
    if(num=="" or int(num)<random_int):
        WriteInFile(random_int)
    else:
        print(random_int)

for i in range(10):
    HighestNumberGame()

