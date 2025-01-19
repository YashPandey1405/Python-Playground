class Parent:
    def __init__(self, Pname,Page):
        print(f"Parent Class Constructor Called....")
        
        self.Pname = Pname
        self.Page = Page
    
    def Display(self):
        print(f"Parent initialized with Name '{self.Pname}' And Age {self.Page}")


class Child(Parent):
    def __init__(self, Pname, Page,name,age):
        super().__init__(Pname,Page)  # Pass 'Pname' & 'Page' to the Parent class
        print(f"Child Class Constructor Called....\n")

        self.name = name
        self.age = age
    
    def Display(self):
        super().Display()
        print(f"Child initialized with Name '{self.name}' And Age {self.age}")

# Example
obj = Child("Prabhash",51,"Yash", 21)
obj.Display()

