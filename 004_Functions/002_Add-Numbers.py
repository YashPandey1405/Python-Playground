# Use Of Default b=10 When Value Of 'b' Is Not Passed.....
def sum(a,b=10): 
    return (a+b)

def TakeNumbers():
    a=int(input("ENTER THE 1st NUMBER ::: "))
    b=int(input("ENTER THE 2nd NUMBER ::: "))
    ans=sum(a,b)
    print(f"SUM OF {a} & {b} IS ::: {ans}")

print(sum(10,20))
print(sum(10))
TakeNumbers()