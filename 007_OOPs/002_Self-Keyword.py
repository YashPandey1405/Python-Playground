class Employee:
    name="Yash Pandey"
    Salery = 12000000

    def details(self):
        print(f"The Employee {self.name} Has Salery Of {self.Salery} LPA....")

    @staticmethod
    def Greet():  
        # 'staticmethod' Means It Doesn't need any Object......
        print("Hello , Myself Yash Pandey")

YashPandey = Employee()
YashPandey.details()
YashPandey.Greet()