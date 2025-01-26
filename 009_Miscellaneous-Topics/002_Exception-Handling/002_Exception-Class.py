# Custom Exception Class
class CustomError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

# Function that raises the custom exception
def check_value(value):
    if value < 0:
        raise CustomError("Negative value is not allowed!", 400)
    elif value == 0:
        raise CustomError("Value cannot be zero!", 401)
    else:
        print(f"Value {value} is valid.")

# Main code to demonstrate exception handling
try:
    num = int(input("Enter a number: "))
    check_value(num)
except CustomError as e:
    print(f"CustomError caught: {e} (Code: {e.code})")
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("Execution completed.")
