import pandas as pd
import os
import time
import re



def login_excel_in():
#excel data to get the locations
    excel_in_path = "WalmartTemp2.xlsx"
    excel_in_open = pd.read_excel(excel_in_path)
    excel_df = pd.DataFrame(excel_in_open)
    
# Normalize to lowercase
    excel_df["Shipper City"] = excel_df['Shipper City'].str.lower().str.replace(" ","-")
    excel_df['Consignee City'] = excel_df['Consignee City'].str.lower().str.replace(" ","-")
    excel_df['Consignee State'] = excel_df['Consignee State'].str.lower()
    excel_df['Shipper State'] = excel_df['Shipper State'].str.lower()
    
    org_des = []
    for index, x in excel_df.iterrows():
        origin_destination = x['Shipper City'] + "-" + x['Shipper State'] + "~" + x['Consignee City'] + "-" + x['Consignee State'] + "~" + "Van"
        org_des2 = org_des.append(origin_destination)

    return org_des


    

