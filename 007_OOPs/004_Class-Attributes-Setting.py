class Programmer:
    company = "Microsoft"
    # Constructor....
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

    def Details(self):
        print(f"{self.name} Works In {self.company} Company At Salary Of {self.salary} And Has Pin {self.pin}\n")

    @staticmethod
    def Greet():
        print("Welcome To Microsoft")


p = Programmer("Yash", 1200000, 245001)
p.Greet()
p.Details()
# print(p.name, p.salary, p.pin, p.company)
r = Programmer("Divyam", 1200000, 245001)
r.Greet()
r.Details()
# print(r.name, r.salary, r.pin, r.company)