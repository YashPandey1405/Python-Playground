name=input("ENTER YOUR NAME ::: ")
age=int(input("ENTER YOUR AGE ::: "))

if(age>18):
    print(f"\"{name}\" IS Eligible To Vote....")
elif(age<0):
    print(f"\"{name}\" Has Entered Negative Age....")
else: 
    print(f"\"{name}\" IS Not Eligible To Vote....")

print("\nEnd Of Program")