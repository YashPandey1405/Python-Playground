import json

data = [
    {"ID": 1, "Name": "John Doe", "Age": 28, "Department": "Engineering", "Salary": 75000},
    {"ID": 2, "Name": "Jane Smith", "Age": 34, "Department": "Marketing", "Salary": 68000},
    {"ID": 3, "Name": "Robert Brown", "Age": 25, "Department": "Finance", "Salary": 58000},
    {"ID": 4, "Name": "Lisa Johnson", "Age": 29, "Department": "Human Resources", "Salary": 62000},
    {"ID": 5, "Name": "Michael Lee", "Age": 32, "Department": "Engineering", "Salary": 80000},
    {"ID": 6, "Name": "Sophia Wilson", "Age": 26, "Department": "Marketing", "Salary": 59000},
    {"ID": 7, "Name": "James Taylor", "Age": 31, "Department": "Finance", "Salary": 72000},
    {"ID": 8, "Name": "Emily Davis", "Age": 27, "Department": "Human Resources", "Salary": 61000},
    {"ID": 9, "Name": "David Clark", "Age": 30, "Department": "Engineering", "Salary": 77000},
    {"ID": 10, "Name": "Olivia Martinez", "Age": 33, "Department": "Marketing", "Salary": 70000},
]

# Writing data to a JSON file
with open("example.json", "w") as file:
    json.dump(data, file, indent=4)  # Use indent=4 for better readability

# Reading data from the JSON file
with open("example.json", "r") as file:
    loaded_data = json.load(file)
    for entry in loaded_data:
        print(entry)
