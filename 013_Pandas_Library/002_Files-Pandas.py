import pandas as pd # type: ignore

# **Excel File Related Methods**

# pd.read_excel() - Reads an Excel file
# Example: df_excel = pd.read_excel('sample_data.xlsx', sheet_name='Sheet1')
# You can read multiple sheets by passing a list to sheet_name
# df_excel_multiple = pd.read_excel('sample_data.xlsx', sheet_name=['Sheet1', 'Sheet2'])
# print(df_excel_multiple)

# pd.ExcelFile() - Opens an Excel file for inspection
# excel_file = pd.ExcelFile('sample_data.xlsx')
# print(excel_file.sheet_names)  # List all sheet names

# pd.DataFrame.to_excel() - Writes DataFrame to an Excel file
# df.to_excel('output.xlsx', index=False)

# **HTML File Related Methods**

# pd.read_html() - Reads HTML tables from a URL or HTML file
# Example URL: https://www.w3schools.com/html/html_tables.asp
# url = "https://www.w3schools.com/html/html_tables.asp"
# df_html = pd.read_html(url)
# print("\nHTML Table from URL:")
# print(df_html[0])  # Get the first table

# pd.DataFrame.to_html() - Converts DataFrame to HTML table
# df_html_table = df.to_html()  # Returns HTML string
# with open('table.html', 'w') as f:
#     f.write(df_html_table)

# **JSON File Related Methods**

# pd.read_json() - Reads a JSON file into a DataFrame
# Example: df_json = pd.read_json('data.json')
# print("\nJSON DataFrame:")
# print(df_json)

# pd.DataFrame.to_json() - Converts DataFrame to JSON format
# df_json_output = df.to_json(orient='records')  # 'records' for list of dictionaries
# print("\nJSON Data:")
# print(df_json_output)

# pd.json_normalize() - Flattens nested JSON objects into a DataFrame
# Nested JSON example:
# nested_json = {'id': 1, 'name': 'Alice', 'address': {'city': 'New York', 'state': 'NY'}}
# df_normalized = pd.json_normalize(nested_json)
# print("\nNormalized JSON DataFrame:")
# print(df_normalized)
