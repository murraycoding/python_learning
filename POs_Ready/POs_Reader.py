'''
Modules
'''

from Files_in_Folder import ListFiles_Folder
from getPos_text import *
import pandas as pd
import os
import re
import fitz
from ValidationFile import *

''''
Code
'''
# get the files name in the folder
yfolder_path = "/Users/jmutcap/OneDrive - CUEBITZ LLC/Walmart 2025/Walmart POs"
Files_Listed = ListFiles_Folder(yfolder_path)

#stored data
Stored_values_path = "/Users/jmutcap/OneDrive - CUEBITZ LLC/ValidatePOs.xlsx"
Stored_val = pd.read_excel(Stored_values_path)
Stored_values = pd.DataFrame(Stored_val)

zfile_path = '/Users/jmutcap/OneDrive - CUEBITZ LLC/POsData.xlsx' #file that store the PO data

#get the data on each PO in the folder zfile_path
for x in Files_Listed:
    if x in Stored_values['ID'].values:
        print("Value is already in the list")
    else:
        try:
            getPOs_text(x, yfolder_path+ "/" + x, zfile_path)#first variable PO file name, second variable path where the PO files are stored, third variable is the output file with the data
            new_rows = pd.DataFrame({"ID": [x]})  # Correctly create a new row with a list
            Stored_values = pd.concat([Stored_values, new_rows], ignore_index=True)
            # Save the updated DataFrame back to the Excel file
            Stored_values.to_excel(Stored_values_path, index=False, engine='openpyxl')
        except ValueError as e:
            print(f"ValueError encountered for file {x}: {e}") #the file and the error encountered
        
        except Exception as e:
            print(f"An error occurred while processing {x}: {e}")
      
      


