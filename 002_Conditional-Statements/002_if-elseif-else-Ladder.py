# Example: Grading system based on marks
name=input("ENTER YOUR NAME ::: ")
marks = int(input("Enter your marks: "))

if(marks >= 90):
    print(f"{name} Got Grade: A+....")
elif(marks >= 80):
    print(f"{name} Got Grade: A....")
elif(marks >= 70):
    print(f"{name} Got Grade: B....")
elif(marks >= 60):
    print(f"{name} Got Grade: C....")
elif(marks >= 50):
    print(f"{name} Got Grade: D....")
else:
    print(f"{name} Got Grade: F (Fail)")


print("\nEnd Of Program")