def sum(num):
    if(num==1):
        return 1
    return num+sum(num-1)

num=int(input("ENTER THE NUMBER ::: "))
ans=sum(num)
print(f"The Sum Of First {num} Natural Numbers Is ::: {ans}")