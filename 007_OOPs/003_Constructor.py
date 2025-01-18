class Employee:
    name="Employee"
    salery=100000

    # def __init__(self,Ename):   # Dunder Method.....
    #     print("This Is The Constructor Of Student Class....")
    #     self.name=Ename

    # Syntax Of Constructor In Python With 2 Parameter.....
    def __init__(self,Ename,Esalery):   # Dunder Method.....
        print("This Is The Constructor Of Student Class....")
        self.name=Ename
        self.salery=Esalery
    
    def Details(self):
        print(f"The Employee {self.name} Has Salery Of {self.salery} LPA....")

Yash=Employee("YashPandey",1200000)
Yash.Details()

print("\n")

Divyam=Employee("Divyam",2000000)
Divyam.Details()
        