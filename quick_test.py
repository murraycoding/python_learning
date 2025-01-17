
import pandas as pd

data_file_path = '/Users/jmutcap/OneDrive - CUEBITZ LLC/Soils_Main_sheet.xlsx'
data_file_open = pd.read_excel(data_file_path)
data_file_df = pd.DataFrame(data_file_open)


for index, row in data_file_df.iterrows():
    print(row['FB#'])
    print(row['TotalRevenue'])
    
