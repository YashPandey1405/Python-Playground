# Implementation Of Abstraction & Encapsulation.....

class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    # @property: Defines a method as a read-only property
    # It Allows access like an attribute without using parentheses.
    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    # @name.setter: Allows setting a value to the property
    # It Enables controlled modification of the attribute.
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Harry Khan"
print(e.fname, e.lname)

e.show()