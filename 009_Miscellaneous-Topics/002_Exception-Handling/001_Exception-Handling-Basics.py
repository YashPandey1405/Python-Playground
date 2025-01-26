End=int(input("Enter The End Number : "))

try:
    for i in range(End, 0, -1): 
        num = int(50 / i)
        print(num)
except ZeroDivisionError as e:
    print("Division by zero occurred: ", e)
except Exception as e:
    print("An error occurred: ", e)
else:
    print("No errors occurred....")  
finally:
    print("This will always run......")