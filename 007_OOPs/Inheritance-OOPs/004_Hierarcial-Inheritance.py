class Parent:
    def __init__(self, Pname, Page):
        print(f"Parent Class Constructor Called....")
        self.Pname = Pname
        self.Page = Page
    
    def Display(self):
        print(f"Parent initialized with Name '{self.Pname}' And Age {self.Page}")

class Son(Parent):
    def __init__(self, Pname, Page, name, age):
        super().__init__(Pname, Page)
        print(f"Son Class Constructor Called....\n")
        self.name = name
        self.age = age

    def Display(self):
        super().Display()
        print(f"Son initialized with Name '{self.name}' And Age {self.age}")

class Daughter(Parent):
    def __init__(self, Pname, Page, name, age):
        super().__init__(Pname, Page)
        print(f"Daughter Class Constructor Called....\n")
        self.name = name
        self.age = age

    def Display(self):
        super().Display()
        print(f"Daughter initialized with Name '{self.name}' And Age {self.age}")

# Example
obj1 = Son("Prabhash", 51, "Yash", 21)
obj1.Display()

print("\n")

obj2 = Daughter("Prabhash", 51, "Isha", 19)
obj2.Display()
