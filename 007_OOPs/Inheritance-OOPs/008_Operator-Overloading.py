class Number:
    def __init__(self, n):
        self.n = n

    """Overload the + operator to add two Number objects."""
    def __add__(self, other):
        return Number(self.n + other.n)

    """Overload the - operator to subtract one Number object from another."""
    def __sub__(self, other):
        return Number(self.n - other.n)

    """Overload the * operator to multiply two Number objects."""
    def __mul__(self, other):
        return Number(self.n * other.n)

    """Overload the / operator to divide one Number object by another."""
    def __truediv__(self, other):
        if (other.n == 0):
            raise ValueError("Division by zero is not allowed.")
        
        return Number(self.n / other.n)

    """Define how the object is displayed when printed."""
    def __str__(self):
        return str(self.n)

n = Number(10)
m = Number(5)

print("Addition:", n + m)       
print("Subtraction:", n - m)   
print("Multiplication:", n * m) 
print("Division:", n / m)      
