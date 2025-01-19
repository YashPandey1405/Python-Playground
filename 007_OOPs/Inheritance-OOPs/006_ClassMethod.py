# The `@classmethod` decorator in Python defines a method that belongs to the class rather than an instance. 
# It takes the class (`cls`) as its first parameter, allowing access to class-level attributes and methods.

class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()