'''
i=0
while(i<=10):
    print(i)
    i+=1
'''

i = 0  

while i <= 100:
    if i == 90:
        print("Value is 90: Thus break the loop....\n")
        break  # Pata Hai Bhai.....
    if i == 50:
        print("Value is 50: Thus skip this iteration of i=50 ....")
        i += 10  
        continue  # Pata Hai Bhai.....
    print(i)
    i += 10  # Increment i for the next iteration

