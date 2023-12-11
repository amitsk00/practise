

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 


# Replace these values with your information
# form_url = "https://docs.google.com/forms/d/e/1FAIpQLSc70uV8e-kP5lR9x3-4q4X2j63n5yH7l-sY840zK3u2Y7A/viewform"
form_url = "https://forms.gle/cU8JHKxChNcB9wzR9"
name_field_id = "i1"
email_field_id = "i5"
message_field_id = "i9"
submit_button_xpath = "//*[@id='lSvzH']/div/div/div/span"

# Configure browser options
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run in headless mode for background execution

# Create a new Chrome session
driver = webdriver.Chrome(options=options)

# Open the Google form URL
driver.get(form_url)

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, name_field_id)))
print("got form")


# Fill the form fields

try:
# name_field = driver.find_element_by_id(name_field_id)
# name_field = driver.find_element(By.ID , name_field_id)
# name_field.send_keys("Your Name")

    name_field = driver.find_elements(By.CLASS_NAME , "whsOnd zHQkBf")
    name_field.insert(0,"Amit")

    # x = driver.find_element(By.CLASS_NAME , "whsOnd zHQkBf" )
    # x.send_keys("Amit")

    print("Added name")


except:
    print("error ...")


try:
    # email_field = driver.find_element_by_id(email_field_id)
    # email_field = driver.find_element(By.ID , email_field_id)
    # email_field.send_keys("Coffee")
    snack_field = driver.find_elements(By.CLASS_NAME , "vRMGwf oJeWuf")
    # print(snack_field.count())

    snack_field.insert(0,"Coffee")    
    print("Added coffee")

    # message_field = driver.find_element_by_id(message_field_id)
    # message_field = driver.find_element(By.ID , message_field_id)
    # message_field.send_keys("Veg")
    # food_field = driver.find_element(By.CLASS_NAME , "vRMGwf oJeWuf")
    snack_field.insert(1,"Veg")
    print("Added veg")
except:
    print("Errrrrorrr")

# print(snack_field.pop() )


# Submit the form
# submit_button = driver.find_element_by_xpath(submit_button_xpath)
# submit_button = driver.find_element(By.CLASS_NAME , "NPEfkd RveJvd snByac")
# submit_button.click()

# Close the browser
# driver.quit()

time.sleep(10)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, name_field_id)))
print("Form submitted successfully!")
