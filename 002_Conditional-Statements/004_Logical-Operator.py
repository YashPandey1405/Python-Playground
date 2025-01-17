# Logical Operator Are 'and' , 'or' , 'not'....
a=int(input("Enter The 1st Number ::: "))
b=int(input("Enter The 2nd Number ::: "))
c=int(input("Enter The 3rd Number ::: "))

if((a>b) and (a>c)):
    print("The Largest Number Is ::: ",a)
elif((b>a) and (b>c)):
    print("The Largest Number Is ::: ",b)
else:
    print("The Largest Number Is ::: ",c)

