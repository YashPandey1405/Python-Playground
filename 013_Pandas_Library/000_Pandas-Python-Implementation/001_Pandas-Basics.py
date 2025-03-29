import pandas as pd # type: ignore

# Reading the CSV file
df = pd.read_csv('/mnt/data/001_sample_file.csv')

# Displaying the DataFrame
print("Original DataFrame:")
print(df)

# Reading CSV file without headers (header=None)
df_no_header = pd.read_csv('/mnt/data/001_sample_file.csv', header=None)
print("\nCSV Without Header:")
print(df_no_header)

# Skipping first 3 rows
df_skip_rows = pd.read_csv('/mnt/data/001_sample_file.csv', skiprows=3)
print("\nCSV After Skipping First 3 Rows:")
print(df_skip_rows)

# Selecting specific columns (Name and Salary)
df_selected_cols = pd.read_csv('/mnt/data/001_sample_file.csv', usecols=['Name', 'Salary'])
print("\nSelected Columns - Name and Salary:")
print(df_selected_cols)

# Series vs DataFrame
print("\nSeries Example:")
series_example = pd.Series([1, 2, 3, 4, 5])
print(series_example)

print("\nDataFrame Example:")
df_example = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [40, 50, 60]
})
print(df_example)

# Resetting the index
df_reset_index = df.reset_index(drop=True)
print("\nDataFrame After Resetting Index:")
print(df_reset_index)

# .head() and .tail() methods
print("\nFirst 3 Rows using .head():")
print(df.head(3))

print("\nLast 2 Rows using .tail():")
print(df.tail(2))

# .info() to see column datatypes
print("\nInfo About DataFrame:")
df.info()

# Converting Series to DataFrame (Example of column conversion)
df_series_to_df = pd.Series([100, 200, 300], name="New_Column")
df_converted = pd.DataFrame(df_series_to_df)
print("\nConverted Series to DataFrame:")
print(df_converted)

# Multiple Column Selection
print("\nMultiple Columns Selection - Name and Age:")
print(df[['Name', 'Age']])
