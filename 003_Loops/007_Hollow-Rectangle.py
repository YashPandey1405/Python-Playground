m=int(input("ENTER THE LENGTH ::: "))
n=int(input("ENTER THE BREADTH ::: "))

print("\n")
for i in range(m):
    if((i==0) or (i==m-1)):
        for j in range(0,n):
            print("*",end=" ")
    else:
        print("*",end=" ")
        for j in range(1,n-1):
            print(" ",end=" ")
        print("*",end=" ")
    print()