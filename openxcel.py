import pandas as pd

# Sample data
data = {'Column1': [1, 2, 3],
        'Column2': ['a', 'b', 'c']}

# Create a DataFrame
df = pd.DataFrame(data)

# Write DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)

# ----------------------------------------------------------------------------------------------------------

# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active

# data = [
#     ["Name", "Age", "Course"],
#     ["Rohan", 18, "Programmimng"],
#     ["Mohan", 20, "Data Analytics"],
#     ["Sohan", 16, "Multimedia"]
# ]

# for row in data:
#     sheet.append(row)
# wb.save("example.xlsx")
