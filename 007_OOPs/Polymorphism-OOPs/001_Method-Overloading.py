# Method overloading doesn't work in Python because it uses **dynamic typing** and allows only the **last defined method** with the same name 
# to persist in a class. Instead, Python achieves similar behavior using default arguments, `*args`, or `**kwargs`.

class Numbers:
    def display(self):   # It Willn't Work....
        print("No Input Parameter Is Been Passed....")
    def display(self,a=10):   # It Willn't Work....
        print(f"1 Input Parameter a={a} Is Been Passed....")
    def display(self,a=10,b=20):  # It Will Only Work....
        print(f"2 Input Parameter a={a} & b={b} Is Been Passed....")

# In Python , The Last Method Overrides All Previous Methods....
obj=Numbers()
obj.display()
obj.display(10)
obj.display(10,20)