import os
import pandas as pd
import fitz
import time
import re
from POs_Ready import Files_in_Folder, Watch_Folder

xfile_path = '' #excel file path with the data extracted
yfile_path = '' #pdf folder path
zfile_path = '' #excel file path with the data to be validated

#Check the files in the folder with all the rate confirmations
Files_in_Folder.ListFiles_Folder(yfile_path)

#validation data stored in an excel file
Val_data = pd.read_excel(zfile_path)
Val_data_df = pd.DataFrame(Val_data)





