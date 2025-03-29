import pandas as pd # type: ignore

# Creating a sample DataFrame with numerical and categorical data
data = {
    "Age": [25, 30, 35, 40, 28],
    "Salary": [50000, 60000, 75000, 80000, 65000],
    "Department": ["HR", "IT", "IT", "HR", "Finance"]
}

df = pd.DataFrame(data)

# Convert the 'Department' column to a categorical type
df["Department"] = pd.Categorical(df["Department"])

# Using describe() to get summary statistics (only numerical columns by default)
print("Numerical Summary:\n", df.describe())

# Using describe() to include categorical data
print("\nIncluding Categorical Data:\n", df.describe(include="category"))

# Display the categorical column's properties
print("\nCategorical Data Info:\n", df["Department"].describe())
