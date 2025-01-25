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
from selenium.webdriver.support.ui import Select
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
tms_button = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'text-center') and text()='TMS']"))
)

# Scroll into view if the element is off-screen
driver.execute_script("arguments[0].scrollIntoView(true);", tms_button)

#click the TMS button
tms_button.click()
print("TMS tile clicked successfully.")
time.sleep(20)

# Switch to the newly opened tab 
new_tab = driver.window_handles[-1]  # The last tab opened
driver.switch_to.window(new_tab)

'''
BEGINNING OF THE LOOP
'''
data_file_path = '/Users/jmutcap/OneDrive - CUEBITZ LLC/Soils_Main_sheet.xlsx'
data_file_open = pd.read_excel(data_file_path)
data_file_df = pd.DataFrame(data_file_open)

for index, row in data_file_df.iterrows():
    try:
        #search for the shipment
        #Locate the search bar using its placeholder attribute
        search_bar = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, "global-search-input"))
        )

        search_bar.click()
        search_bar.send_keys(row['FB#'])
        search_bar.send_keys(Keys.RETURN)
        print("Load searched")

        time.sleep(5)

        # Wait for the button to become clickable
        assign_customer_rate_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@title='Assign Customer Rate']"))
        )
        # Scroll into view if the element is off-screen
        
        # Click the button
        assign_customer_rate_button.click()

        time.sleep(10)

        # Wait for the dropdown to be clickable
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='priceSheet.charges.0.commodity']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        # Click the dropdown to open it
        dropdown.click()


        # Select the option "CONSUMER GOODS OR APPLIANCES"
        consumer_goods_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[text()='CONSUMER GOODS OR APPLIANCES']"))
        )

        # Click the desired option
        consumer_goods_option.click()
        dropdown.click()
        dropdown.send_keys(Keys.TAB)

        time.sleep(1)
        #consumer_goods_option.send_keys(Keys.RETURN)
        #time.sleep(20)
        # Click on the input to trigger class change
        # Wait for the input field to be visible and clickable
        # Locate the parent row for the dropdown (e.g., 'Per Mile')

        ''' #this code will change the dropdown for the rate from flat rate to RPM

        parent_row = driver.find_element(By.XPATH, "//tr[.//span[text()='Flat Rate']]")

        # Locate the dropdown inside the parent row
        dropdown = parent_row.find_element(By.CSS_SELECTOR, "div.mg-input.mg-select")

        # Click to trigger 'focused' class on the dropdown
        dropdown.click()

        # Wait for the dropdown to get focused
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.mg-input.mg-select.focused"))
        )

        # Now select the option 'Per Mile'
        select = dropdown.find_element(By.TAG_NAME, "select")
        select.send_keys("PM")
        '''
        # Wait for the rate input box to be focused

        # Wait for the rate input to have the 'focused' class
        # Wait for the div with class 'mg-input focused' to appear
        rate_input_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.mg-input.focused"))
        )

        # Try to find the input inside this div by its type
        rate_input = rate_input_div.find_element(By.CSS_SELECTOR, "input[type='text']")
        rate_input.click()
        rate_input.clear()
        rate_input.send_keys(row['TotalRevenue'])
        rate_input.send_keys(Keys.TAB)
        print('Rate Entered')
        # Click to trigger 'focused' class on the dropdown
        # Locate the parent row for the dropdown (e.g., 'Fuel Surcharge')
        parent_row = driver.find_element(By.XPATH, "//tr[.//span[text()='Fuel Surcharge']]")

        # Locate the dropdown inside the parent row
        dropdown2 = parent_row.find_element(By.CSS_SELECTOR, "div.mg-input.mg-select")

        # Click to trigger 'focused' class on the dropdown
        dropdown2.click()

        # Wait for the dropdown to get focused
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.mg-input.mg-select.focused"))
        )

        # Now select the option 'PerMile'
        select = dropdown2.find_element(By.TAG_NAME, "select")
        select.send_keys("PM")

        select.click()
        select.send_keys(Keys.SHIFT + Keys.TAB)

        rate_input_div2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.mg-input.focused"))
        )

        # Try to find the input inside this div by its type
        rate_input2 = rate_input_div2.find_element(By.CSS_SELECTOR, "input[type='text']")
        rate_input2.click()
        rate_input2.clear()
        rate_input2.send_keys("0.24")
        rate_input2.send_keys(Keys.TAB)
        
        print("Fuel Rate entered")

        save_rate = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ux-button.ux-select-button.ux-button-primary.ux-button-solid"))
        )
        save_rate.click()
        
        print("Rate Saved")
        # Locate the input field for the rate
        # rate_input = driver.find_element(By.NAME, "charge.YB18JOM0tb.rate")
        # rate_input.send_keys(Keys.TAB)
        # rate_input.clear()
        # rate_input.send_keys('1')

        # #charge.3O_jeyO0mJ.rate
        # fuel_rate_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@name='charge.3O_jeyO0mJ.rate']"))
        # )
        # fuel_rate_input.clear()
        # fuel_rate_input.send_keys('1')


        time.sleep(6)
    except:
        print(f"Error on {row['FB#']}")
        driver.refresh()
        
        # #hovering the rate field
        # hover_element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "mg-popover-hover-trigger"))
        # )

        # # Use ActionChains to hover over the element
        # actions = ActionChains(driver)
        # actions.move_to_element(hover_element).perform()


        # #<span class="mg-link-text">Rate</span>
        # rate_click = driver.find_element(By.XPATH, "//span[contains(text(), 'Rate')]")
        # rate_click.click()


        # rate_click = driver.find_element(By.XPATH, "//span[contains(text(), 'Add manual rate')]")
        # rate_click.click()

        '''
        #open the shipement
        #<span class="loadheader-identity-linked">EL4740098</span>
        open_load_click = WebDriverWait(driver,20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "loadheader-identity-linked"))
            
        )
        open_load_click.click()
        #time.sleep(20)
        print("Load opened")




        #change to the new windows opened
        # Get the handle of the original window
        original_window = driver.current_window_handle

        # Wait for the new window to open and switch to it
        WebDriverWait(driver, 20).until(EC.new_window_is_opened([original_window]))
        new_window = [window for window in driver.window_handles if window != original_window][1]
        driver.switch_to.window(new_window)
        time.sleep(90)


        #Click more on the shipment to see special notes or instructions
        #<span class="mg-ux-link-content metric-uxlink-content">More</span>

        more_button = WebDriverWait(driver,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".mg-ux-link-text-hold.metric-simpleNote-toggleLink-editable"))
        )

        more_button.click()

        # Locate the field More and extract the text
        instructions_field = driver.find_element(By.CLASS_NAME, "simple-note-comments")
        instructions_text = instructions_field.text
        print(instructions_text)

        #Check all the elements in the website
        # all_elements =  driver.find_elements(By.XPATH, "//*")

        # for element in all_elements:
        #     try:
        #         print(f"Tag: {element.tag_name}, Text: {element.text}, ID: {element.get_attribute('id')}, Class: {element.get_attribute('class')} ")
        #     except Exception as e:
        #         print(e)
                


        time.sleep(900)



                

        # Scroll the search bar into view if needed
        # driver.execute_script("arguments[0].scrollIntoView(true);", search_bar)

        # # Click on the search bar and enter text
        # search_bar.click()
        # search_bar.clear()  # Clear any existing text in the input field
        # search_bar.send_keys("8302591")

        '''