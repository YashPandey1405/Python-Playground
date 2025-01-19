class GrandParent:
    def __init__(self, Gname,Gage):
        print(f"GrandParent Class Constructor Called....")
        
        self.Gname = Gname
        self.Gage = Gage
    
    def Display(self):
        print(f"GrandParent initialized with Name '{self.Gname}' And Age {self.Gage}")

class Parent(GrandParent):
    def __init__(self,Gname,Gage,Pname,Page):
        super().__init__(Gname,Gage)
        print(f"Parent Class Constructor Called....")
        
        self.Pname = Pname
        self.Page = Page
    
    def Display(self):
        super().Display()
        print(f"Parent initialized with Name '{self.Pname}' And Age {self.Page}")


class Child(Parent):
    def __init__(self,Gname,Gage,Pname, Page,name,age):
        super().__init__(Gname,Gage,Pname,Page)
        print(f"Child Class Constructor Called....\n")

        self.name = name
        self.age = age
    
    def Display(self):
        super().Display()
        print(f"Child initialized with Name '{self.name}' And Age {self.age}")

# Example
obj = Child("Hira Lal",84,"Prabhash",51,"Yash", 21)
obj.Display()

