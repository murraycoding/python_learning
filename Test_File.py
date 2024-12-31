import pandas as pd

#Search and read the excel file
file_path = 'Wal.xls'
data = pd.read_excel(file_path)

#Display all the columns in the sheet
#print(data.columns.tolist()) 

test = data.columns.tolist()

count = 0
for i in test:
    count += 1
    print(f"{count}: {i}")

#select the columns you want to see
data_entry = input("Which columns you want to see? Enter the numbers separated by a comma: ")
data_list = []
data_list = data_entry.split(',')

column_todisplay = []
for x in data_list:
    column_todisplay.append(test[int(x)-1])
    
print(column_todisplay)
test_data = data[column_todisplay]



# Select specific columns
#columns_to_display = ['Ref: Freight Bill Number', 'Ref: Freight Bill Number', 'Shipper City', 'Shipper State',]  # Replace with your actual column names
#selected_data = data[columns_to_display]

# Display the first few rows of the selected columns
print(test_data.head(25))

# # Define the value to find
# value_to_find = 'SomeValue'  # Replace with the value you're looking for
# column_to_search = 'ColumnName'  # Replace with the name of the column you want to search in

# # Find the row where the value appears
# row = data.loc[data[column_to_search] == value_to_find]

# # Display the row(s)
# print(row)