from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, StaleElementReferenceException
from login_excel_in import *
import traceback
import time
from datetime import datetime
from login_text_cat import *
import pickle  # used to save website cookies

# Set up Chrome options for headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (optional, recommended for headless)
chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (needed on some environments)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def dat_login(x):
# Set up the WebDriver
    
    driver = x


    driver.get("https://iq.prod.dat.com/rateview/laredo-tx~colorado-spgs-co~van")

    full_page_text = driver.page_source
    print("Full page text:", full_page_text[:500])  # Print the first 500 characters for reference

    print("Waiting for the username field...")
    # Explicitly wait until the username field is located and visible
    username_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    print("Username field found")

    # Locate the username field and send keys
    username_field.send_keys("jurena@smpstar.com")  # Replace with your username
    username_field.send_keys(Keys.RETURN)  # Submit the form
    print("Username submitted")

    # Wait for the next element to load (e.g., password field or login button)
    print("Waiting for the password field...")
    password_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, "password"))  # Replace with the appropriate element
    )
    print("Next page element loaded (password field or next button).")

    password_field.send_keys("Landstaronline.123")  # Replace with your password
    password_field.send_keys(Keys.RETURN)  # Submit the form
    print("Password submitted")

    # Diagnostic sleep to observe what's happening after submission
    print("Waiting for the next page to load...")
    time.sleep(50)  # Increase

    # Save the cookies after logging in
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    # Refresh the page to apply the cookies
    driver.refresh()

    try:
        while True:  # Loop until the pop-up disappears
            try:
                # Wait for the "LOGIN ANYWAY" button to be clickable
                login_anyway_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'LOGIN ANYWAY')]"))
                )

                # Scroll the button into view
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", login_anyway_button)
                    time.sleep(1)  # Allow time for scrolling
                except StaleElementReferenceException:
                    print("Element became stale after scrolling. Re-locating...")
                    continue  # Restart the loop to re-locate the button

                # Attempt to click the button
                try:
                    login_anyway_button.click()
                    print("Clicked 'LOGIN ANYWAY' button.")
                    time.sleep(1)  # Short pause to allow changes to propagate
                except ElementClickInterceptedException:
                    print("Click intercepted. Attempting to click using JavaScript.")
                    # Use JavaScript to click the button
                    driver.execute_script("arguments[0].click();", login_anyway_button)
                    print("Clicked 'LOGIN ANYWAY' using JavaScript.")
                    time.sleep(1)

                # Break the loop if the button is no longer visible
                try:
                    if not login_anyway_button.is_displayed():
                        print("Button is no longer visible. Breaking loop.")
                        break
                except StaleElementReferenceException:
                    print("Button is no longer in the DOM. Breaking loop.")
                    break

            except TimeoutException:
                print("Button not found within the timeout period. Exiting loop.")
                break
    except Exception as e:
        traceback.print_exc()

dat_login(driver)
# pude_location = []


origin_des = login_excel_in()


for o in origin_des:
    try:
        url_path = (f"https://iq.prod.dat.com/rateview/{o}")  # Replace with your target URL
        driver.get(url_path)
        try:
                WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
                username_field_bool = True
        except:
                username_field_bool = False
        if username_field_bool == True:
                print("Loop has been logged out, trying again")
                dat_login(driver)
                driver.get(url_path)
        else:
        # Diagnostic sleep to observe what's happening after submission
                print("Waiting for the next page to load...")
                time.sleep(15)  # Increase sleep time to see the result

                # Get specific element text
                element_text = WebDriverWait(driver, 30).until(
                    EC.visibility_of_element_located((By.ID, "rv-spot-rate"))  # Replace with the actual ID
                ).text
                # print("Specific element text:", element_text)
                elements_extracted = element_text.split("\n")
                # [item for item in elements_extracted if item not in ['trending_up', 'trending_down','domain','description']]
                #print(elements_extracted)
                time.sleep(5)
                # Initialize variables with default value
                daily_15_rate = 0
                daily_15_minmax = 0
                daily_15_domain = 0
                daily_15_company = 0

                daily_3_rate = 0
                daily_3_minmax = 0
                daily_3_domain = 0
                daily_3_company = 0

                daily_30_rate = 0
                daily_30_minmax = 0
                daily_30_domain = 0
                daily_30_company = 0

                daily_7_rate = 0
                daily_7_minmax = 0
                daily_7_domain = 0
                daily_7_company = 0
                
                today_date = datetime.today().strftime('%Y-%m-%d')
                
                removed_words = ["trending_up", "trending_down", "description", "domain"]
            
                elements_extracted = [word for word in elements_extracted if word not in removed_words]

                for rate in elements_extracted:
                    try:
                        if "15 Day" in rate:
                            daily_15_rate = (elements_extracted[elements_extracted.index(rate) + 1]).replace('$','').replace(',','').strip()
                            daily_15_minmax = elements_extracted[elements_extracted.index(rate) + 2]
                            daily_15_domain = elements_extracted[elements_extracted.index(rate) + 3][0]
                            daily_15_company = elements_extracted[elements_extracted.index(rate) + 4][0]

                        if "3 Day" in rate:
                            daily_3_rate = (elements_extracted[elements_extracted.index(rate) + 1]).replace('$','').replace(',','').strip()
                            daily_3_minmax = elements_extracted[elements_extracted.index(rate) + 2]
                            daily_3_domain = elements_extracted[elements_extracted.index(rate) + 3][0]
                            daily_3_company = elements_extracted[elements_extracted.index(rate) + 4][0]

                        if "30 Day" in rate:
                            daily_30_rate = (elements_extracted[elements_extracted.index(rate) + 1]).replace('$','').replace(',','').strip()
                            daily_30_minmax = elements_extracted[elements_extracted.index(rate) + 2]
                            daily_30_domain = elements_extracted[elements_extracted.index(rate) + 3][0]
                            daily_30_company = elements_extracted[elements_extracted.index(rate) + 4][0]

                        if "7 Day" in rate:
                            daily_7_rate = (elements_extracted[elements_extracted.index(rate) + 1]).replace('$','').replace(',','').strip()
                            daily_7_minmax = elements_extracted[elements_extracted.index(rate) + 2]
                            daily_7_domain = elements_extracted[elements_extracted.index(rate) + 3][0]
                            daily_7_company = elements_extracted[elements_extracted.index(rate) + 4][0]

                    except Exception as e:
                        print(f"Error processing rate {rate}: {e}")
                        continue  # Continue to the next iteration if there is an error

                    # Store the information extracted in a new excel file
                    excel_path_out = '/Users/jmutcap/OneDrive - CUEBITZ LLC/DAT_Rates_Extracted.xlsx'
                    excel_open_out = pd.read_excel(excel_path_out)
                    excel_df = pd.DataFrame(excel_open_out)

                    new_excel_data = pd.DataFrame({
                        'Location': [o],
                        '3DM Rate': [daily_3_rate],
                        'minmax': [daily_3_minmax],
                        'Reported Domain': [daily_3_domain],
                        'Reported Companies': [daily_3_company],
                        '7DM Rate': [daily_7_rate],
                        'minmax2': [daily_7_minmax],
                        'Reported Domain3': [daily_7_domain],
                        'Reported Companies4': [daily_7_company],
                        '15DM Rate': [daily_15_rate],
                        'minmax5': [daily_15_minmax],
                        'Reported Domain6': [daily_15_domain],
                        'Reported Companies7': [daily_15_company],
                        '30DM Rate': [daily_30_rate],
                        'minmax8': [daily_30_minmax],
                        'Reported Domain9': [daily_30_domain],
                        'Reported Companies10': [daily_30_company],
                        'Day': [today_date]
                    })

                    try:
                        excel_Data_existing = pd.read_excel(excel_path_out, engine='openpyxl')
                        excel_combined_data = pd.concat([excel_Data_existing, new_excel_data], ignore_index=True)
                        #print(f"new data added for: {o} on: {today_date}")
                    except FileNotFoundError:
                        excel_combined_data = new_excel_data

                    excel_combined_data.to_excel(excel_path_out, index=False, engine='openpyxl')

    except Exception as e:
        print(f"Error for {o}: {e}")
        traceback.print_exc()

driver.quit()  # Ensure the browser is closed in any case
