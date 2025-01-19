class Mother:
    def __init__(self, MotherName,MotherAge):
        print(f"Mother Class Constructor Called....")
        
        self.MotherName = MotherName
        self.MotherAge = MotherAge
    
    def Display(self):
        print(f"Mother initialized with Name '{self.MotherName}' And Age {self.MotherAge}")

class Father:
    def __init__(self,FatherName,FatherAge):
        print(f"Father Class Constructor Called....")
        
        self.FatherName = FatherName
        self.FatherAge = FatherAge
    
    def Display(self):
        print(f"Father initialized with Name '{self.FatherName}' And Age {self.FatherAge}")


class Child(Mother,Father):
    def __init__(self,MotherName,MotherAge,FatherName, FatherAge,name,age):
        super().__init__(MotherName,MotherAge)
        Father.__init__(self, FatherName,FatherAge)
        print(f"Child Class Constructor Called....\n")

        self.name = name
        self.age = age
    
    def Display(self):
        super().Display()
        Father.Display(self)
        print(f"Child initialized with Name '{self.name}' And Age {self.age}")

# Example
obj = Child("Annu",45,"Prabhash",51,"Yash", 21)
obj.Display()

