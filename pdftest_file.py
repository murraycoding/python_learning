import fitz
import re
import pandas as pd
import os

#variables

pos_weight_qty = []
po = r'\b\d+\b' #r in front of the regex code and then the regex code between ''

# Path to the PDF file
file_path = "897066532-PO-853705.pdf.pdf"
# Open the PDF file
pdf_document = fitz.open("897066532-PO-853705.pdf.pdf")

# Iterate through each page
for page_number in range(len(pdf_document)):
    page = pdf_document[page_number]
    po = r'\b\d{6}\b' #r in front of the regex code and then the regex code between ''
    weight = r'(?i)packages\s+(\d{1,3}(?:,\d{3})*(?:\.\d+)?)'
    qty_pieces = r'\d+\s+Packages'
    trailer = r'(?i)DRYVAN[-\s]*([\d\-]+)'
    
    text = page.get_text()
    match_po = re.findall(po, text)
    match_weight = re.findall(weight, text)
    match_qty_pieces = re.findall(qty_pieces, text)
    match_trailer = re.findall(trailer,text)
    
    #print(text)
    #pos_weight_qty.append((match_po,match_weight,match_qty_pieces,match_trailer))
    #print(pos_weight_qty)
    
    
    # Extract the file name from the full file path
    file_name = os.path.basename(file_path)
    match_ID = re.match(r'^\d{9}', file_name)
    match_ID = match_ID.group()
    
    match_weight2 = float(match_weight[0].replace(',', ''))
    
    new_po = pd.DataFrame({
        
        "ID" : match_ID,
        "PO" : match_po,
        "Weight": match_weight2,
        "Qty": match_qty_pieces,
        "Trailer": match_trailer
        
    })
    
    # Specify the file path where the Excel file will be saved
    output_file_path = '/Users/jmutcap/OneDrive - CUEBITZ LLC/POsData.xlsx'

pos_weight_qty.append((match_po,match_weight,match_qty_pieces,match_trailer))
    # Write the DataFrame to an Excel file (for a new file or new dataframe)
    #new_po.to_excel(output_file_path, index=False, engine='openpyxl')

try:
    po_existing = pd.read_excel(output_file_path, engine='openpyxl')
    # Concatenate the existing data with the new data
    po_combined = pd.concat([po_existing, new_po], ignore_index=True)
except FileNotFoundError:
    # If the file does not exist, we'll just use the new data
    po_combined = new_po

# Write the combined data to the Excel file
po_combined.to_excel(output_file_path, index=False, engine='openpyxl')

print(f"Data appended to {output_file_path}")

print(f"New data appended to {output_file_path}")

print(f"Results saved to {output_file_path}")
    
pos_weight_qty.append((match_po,match_weight,match_qty_pieces,match_trailer))
    
print(pos_weight_qty)
#print(page.get_text())  # Extract text from the page
    
