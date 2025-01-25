import csv

data = [
    ["ID", "Name", "Age", "Department", "Salary"],
    [1, "John Doe", 28, "Engineering", 75000],
    [2, "Jane Smith", 34, "Marketing", 68000],
    [3, "Robert Brown", 25, "Finance", 58000],
    [4, "Lisa Johnson", 29, "Human Resources", 62000],
    [5, "Michael Lee", 32, "Engineering", 80000],
    [6, "Sophia Wilson", 26, "Marketing", 59000],
    [7, "James Taylor", 31, "Finance", 72000],
    [8, "Emily Davis", 27, "Human Resources", 61000],
    [9, "David Clark", 30, "Engineering", 77000],
    [10, "Olivia Martinez", 33, "Marketing", 70000],
]

with open("example.csv", "w",newline="") as file:  # Added newline=""
    writer = csv.writer(file)
    for row in data: 
        writer.writerow(row)

with open("example.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
