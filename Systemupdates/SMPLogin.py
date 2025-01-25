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


def smp_login(x):
    try:
#Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (optional, recommended for headless)
        chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (needed on some environments)

        # Set up the WebDriver
        driver = x

        #open the website
        driver.get("https://www.landstaronline.com/public/login.aspx")

        driver.maximize_window()
        
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
       
        return driver
    except:
        print("Error logging in")

