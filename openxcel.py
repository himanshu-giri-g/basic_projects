import pandas as pd     #alternative module = openpyxl

# Sample data
data = {'Name': ["Rohan","Mohan","Sohan"],
        'Course': ['Python', 'JAVA', 'C++'],
        'Age': [18,21,19]}

# Create a DataFrame
df = pd.DataFrame(data)

# Write DataFrame to an Excel file
df.to_excel('example.xlsx', index=False)