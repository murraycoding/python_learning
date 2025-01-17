from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, StaleElementReferenceException
import traceback
import time
from datetime import datetime
import pickle  # used to save website cookies
import pandas as pd

#Set up Chrome options for headless mode
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (optional, recommended for headless)
chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (needed on some environments)

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#open the website
driver.get("https://www.landstaronline.com/public/login.aspx")

#Login actvitity
print("Waiting for the username field...")
# Explicitly wait until the username field is located and visible
username_field = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.ID, "USER"))
)
print("Username field found")

# Locate the username field and send keys
username_field.send_keys("jurena")  # Replace with your username
username_field.send_keys(Keys.TAB)  # Submit the form
print("Username entered")

# Wait for the next element to load (e.g., password field or login button)
print("Waiting for the password field...")
password_field = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.NAME, "PASSWORD"))  # Replace with the appropriate element
)
print("Next page element loaded (password field or next button).")

password_field.send_keys("320521")  # Replace with your password
password_field.send_keys(Keys.RETURN)  # Submit the form
print("Password submitted")
print("Login Sucessful")

time.sleep(10)


#Define the button, scroll down and click
losm_button = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'text-center') and text()='LOSM']"))
)

# Scroll into view if the element is off-screen
driver.execute_script("arguments[0].scrollIntoView(true);", losm_button)

#click the TMS button
losm_button.click()
print("LOSM tile clicked successfully.")
time.sleep(20)

# # Switch to the newly opened tab 
new_tab = driver.window_handles[-1]  # The last tab opened
driver.switch_to.window(new_tab)

leads = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'LEADS Operating System')]"))
)
leads.click()

#<a href="/losm/menu/menu.xhtml" onclick="openMenuOption('WB0005', '26');return false;">EDI Load Tendering</a>
#Click EDI Tendering

edi_load_tendering = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'EDI Load Tendering')]"))
)
edi_load_tendering.click()

# # Switch to the newly opened tab 
new_tab = driver.window_handles[-1]  # The last tab opened
driver.switch_to.window(new_tab)

# Click to interact with a dropdown
arrow_button = driver.find_element(By.CLASS_NAME, "dijitArrowButtonInner")
arrow_button.click()

# Select the option
walmart_soil = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'WALMART-FIXTURES LRGR')]"))
)
walmart_soil.click()


# Click to interact with a dropdown accepted tender
arrow_button = driver.find_element(By.ID, "statusCodeOther_select")
arrow_button.click()

# accepted_soil = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Accepted Tenders')]"))
# )
#accepted_soil.click()
arrow_button.clear()
arrow_button.send_keys('Accepted Tenders')
arrow_button.send_keys(Keys.TAB)


date_from = driver.find_element(By.ID, 'startDate_dojo_dateBox')
date_from.click()
date_from.clear()
date_from.send_keys('12/20/2024')
date_from.send_keys(Keys.RETURN)

#database or excel data
soils_excel_path = '/Users/jmutcap/OneDrive - CUEBITZ LLC/Soil_rates.xlsx'
soil_excel_open = pd.read_excel(soils_excel_path)
soil_df = pd.DataFrame(soil_excel_open)

'''
LOOP START HERE
'''
count = 0
data_list = []
print("Starting the loop now")
for index, row in soil_df.iterrows():
    try:
        shipment_id = driver.find_element(By.ID, 'shipmentId')
        shipment_id.click()
        shipment_id.clear()
        shipment_id.send_keys(str(int(row['ID2'])))
        shipment_id.send_keys(Keys.RETURN)
        
        time.sleep(2)

        #if there are several options with the same title you can use [1] to get the first one
        view_tender_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//img[@title='View Tender Detail'])[1]"))
        )
        view_tender_button.click()
    except ValueError as e:
        print(f"error: {e}")
    time.sleep(3)

    #data to be extracted (rate, weight, PU Date and freight bill #)
    rate_text = driver.find_element(By.XPATH, "//td[span[text()='Rate']]/following-sibling::td/span").text
    print(rate_text)

    weight_text = driver.find_element(By.XPATH, "//td[span[text()='Weight']]/following-sibling::td/span").text
    print(weight_text)

    freightbill_text = driver.find_element(By.XPATH, "//span[@id='fbNumber']").text
    print(freightbill_text)

    pudate_text = driver.find_element(By.XPATH, "//span[@id='pickupDateTime']").text
    pudate_text = pudate_text.split(" ")[0]
    print(pudate_text)


# Append the data to the list
    soil_df.at[index, 'Rate'] = rate_text
    soil_df.at[index, 'Weight'] = weight_text
    soil_df.at[index, 'PUDate'] = pudate_text
    soil_df.at[index, 'FB'] = freightbill_text

# Convert the list to a DataFrame and append to Excel
    #new_data = pd.DataFrame(data_list, columns=['Rate', 'Weight', 'PUDate', 'FB'])

    # new_data = pd.DataFrame({
    #     'Rate' : [rate_text],
    #     'Weight' : [weight_text],
    #     'PUDate' : [pudate_text],
    #     'FB'  : [freightbill_text]
        
    # })
    
    #new_data = pd.DataFrame(data_list)

    #Cancelbutton
    #cancelButton_button_label
    cancel_button = driver.find_element(By.ID, 'cancelButton_button_label')
    cancel_button.click()
    
    count +=1
    
    soil_df.to_excel(soils_excel_path, index=False, engine='openpyxl')

    # try:
    #         current_soil_file = pd.read_excel(soils_excel_path, engine='openpyxl')
    #     # Concatenate the existing data with the new data
    #         soil_excel_combined = pd.concat([current_soil_file, new_data], ignore_index=True)
    # except FileNotFoundError:
    #     # If the file does not exist, we'll just use the new data
    #         soil_excel_combined_combined = new_data

    # # Write the combined data to the Excel file
    # soil_excel_combined.to_excel(soils_excel_path, index=False, engine='openpyxl')
    
print(f"All the data has been entered: {count}")

# Now append to the existing Excel file
