import pandas as pd
import re
import os
import time


#excel where the information will be store

def login_excel_out():
    excel_path_out = ""
    excel_open_out = pd.read_toexcel(excel_path_out)
    excer_out_df = pd.DataFrame(excel_open_out)
    
    