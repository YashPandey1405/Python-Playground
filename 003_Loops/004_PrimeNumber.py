num=int(input("ENTER THE NUMBER ::: "))

for i in range(2,num):
    if (num%i==0):
        print(f"{num} Is Not A Prime Number.....\n")
        break
    elif(i==(num-1)):
        print(f"{num} Is An Prime Number.....\n")

print("End Of Program")