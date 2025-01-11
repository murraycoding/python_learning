import pandas as pd
import re

file_path = 'Wal.xls'
data = pd.read_excel(file_path)
data2 = pd.DataFrame(data)

#Make a column a key or as the index
data2 = data2.set_index('Ref: Freight Bill Number')

# split into 2 columns
data2[['Location', 'Zip Code']] = data2['Shipper'].str.rsplit(' ', n=1, expand=True)
'''
.str.rsplit(' ', n=1): Splits the string from the right at the last space, ensuring that the location and zip code are separated correctly.

'n=1': Splits into two parts.

expand=True: Expands the split result into separate columns.
[['Location', 'Zip Code']]: Assigns the split results to new columns.
'''
#remove the original column after splitting it
data2 = data2.drop(columns=['Shipper','Shipper Name','Shipper Address'])

#Normalize the data in a column capitalizing the 1st letter
data2['Shipper City'] = data2['Shipper City'].str.capitalize()

#group dataframe by the data in a column
group_data = data2.groupby('Shipper City')

#count the numbers of entries in the group selected in the previous column
grouped_count = group_data.size()

#give a name to the column created with the count
grouped_count_data2 = grouped_count.reset_index(name='Count')

# Normalize all text columns to capitalize
#data2 = data2.applymap(lambda x: x.capitalize() if isinstance(x, str) else x)

#test = data['Carrier Rate Carrier Name']


print(grouped_count_data2)
