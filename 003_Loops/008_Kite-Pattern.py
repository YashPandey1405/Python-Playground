m=int(input("ENTER THE LENGTH ::: "))

print("\n")

# Loop To Print The Upward Pyramid....
for i in range(0,m):
    for j in range(0,m-i):
        print(" ",end=" ")
    for j in range(0,((2*i)+1)):
        print("*",end=" ")
    print()

# Loop To Print The Downward Pyramid....
for i in range(m-2,-1,-1):
    for j in range(0,m-i):
        print(" ",end=" ")
    for j in range(0,((2*i)+1)):
        print("*",end=" ")
    print()