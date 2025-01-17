def Factorial(num):
    if(num<=0):
        return 1
    return num*Factorial(num-1)

num=int(input("ENTER THE NUMBER ::: "))
ans=Factorial(num)
print(f"The Factorial Of {num} Is ::: {ans}")