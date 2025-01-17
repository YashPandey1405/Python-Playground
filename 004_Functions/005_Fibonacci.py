def Fibonacci(num):
    if(num<=1):
        return 1
    return Fibonacci(num-1)+Fibonacci(num-2)

num=int(input("ENTER THE NUMBER ::: "))
ans=Fibonacci(num)
print(f"The Fibonacci Of {num} Is ::: {ans}")

'''
for i in range(10):
    print(f"{i} --> {Fibonacci(i)}")
'''