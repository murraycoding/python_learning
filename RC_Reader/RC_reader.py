import pandas as pd
import re
import fitz
import os

# Excel file 1. path 2. read 3. create dataframe
excel_filepath = 'RC_data.xlsx'
excelfile_read = pd.read_excel(excel_filepath)
excelfile_df = pd.DataFrame(excelfile_read)
print(excelfile_df)

#PDF file
RCPDF_path = 'EL4727997.pdf'
RCPDF_open = fitz.open(RCPDF_path)
'''
After the PDF file is opened, now we can check page by page for the information we need. Before creating the regex pattern to extract 
specific data, we need to extract all the text for every single page in the file to understand the structure of the file
'''

#Check pages and extract text for each one
for page_number in range(len(RCPDF_open)):
        page = RCPDF_open[page_number]
        text = page.get_text()
        #extracted_text = []
        
        #regex patterns
        rate_regex = r'\$\d+\.\d{2}'
        fb_regex = r'#\s{2}\d{7}'
        pu_de_regex = r'Address\s+[A-Za-z0-9\s.]+\s([A-Za-z\s]+,\s[A-Z]{2})'
        pudate_regex = r'\s{2}\d{2}\/\d{2}\/\d{4}'
        carrier_regex = r'Carrier\s+([A-Za-z\s]+)(?=\s+ID)'
        dispatcher_regex = r'Contact Name: ([A-Za-z\s]+)\n'
        #matching regex pattern in the text extracted
        match_rate = re.findall(rate_regex,text)
        match_fb = re.findall(fb_regex,text)
        match_pu_de = re.findall(pu_de_regex,text)
        match_pudate = re.findall(pudate_regex,text)
        match_carrier = re.findall(carrier_regex,text)
        match_dispatcher = re.findall(dispatcher_regex,text)
        #As the file has several pages we use the if statemnt to match just the pages that have a match
        if match_dispatcher:
            #print(match_dispatcher[0])
            dispatcher = match_dispatcher[0]
        if match_rate:
            #print(match_rate[0])
            rate = match_rate[0]
        if match_pu_de:
            #print(match_pu_de[0])
            #print(match_pu_de[1])
            puloc = match_pu_de[0]
            deloc = match_pu_de[1]
        if match_carrier:
            #print(match_carrier[0])
            carrier = match_carrier[0]
        if match_fb:    
            #print(match_fb[0])
            fb = match_fb[0]
        if match_pudate:
            #print(match_pudate[0])
            pudate = match_pudate[0]
        
#extracted_text = [dispatcher, rate, puloc, deloc, carrier, fb, pudate]
#print(extracted_text)
       
newRc_Data = pd.DataFrame({
    
        "Rate" : [rate],
        "FB#" : [fb],
        "PU" : [puloc],
        "DE" : [deloc],
        "PUDate" : [pudate],
        "Carrier" : [carrier],
        "Dispatcher" : [dispatcher]
})

try:
    RcData_existing = pd.read_excel(excel_filepath, engine='openpyxl')
    # Concatenate the existing data with the new data
    Rc_combined = pd.concat([RcData_existing, newRc_Data], ignore_index=True)
except FileNotFoundError:
    # If the file does not exist, we'll just use the new data
    Rc_combined = newRc_Data

# Write the combined data to the Excel file
Rc_combined.to_excel(excel_filepath, index=False, engine='openpyxl')







