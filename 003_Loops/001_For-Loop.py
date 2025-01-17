'''
for i in range(1,10):
    print(i)
'''

for i in range(1,10,2): # Same As i=i+2....
    if(i==9): 
        print("Value Is 9 : Thus Break The Loop....\n")
        break  # Pata Hai Bhai.....
    if(i==5):
        print("Value Is 5 : Thus Skip This Iteration Of i=5 ....")
        continue  # Pata Hai Bhai.....
    print(i)

# Reverse loop from 10 to 1
for i in range(10, 0, -1):
    print(i, end=" ")


lists=["Yash","Gunnu","Isha",29,31.456,True]
for i in range(len(lists)): 
    # By Default Start from 0.....
    print(f"The Value Of lists[{i}] Is ::: {lists[i]}")