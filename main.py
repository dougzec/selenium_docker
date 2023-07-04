from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os



ambiente_local = os.getenv('AMBIENTE') == 'LOCAL'

# setup chrome options
chrome_options = webdriver.ChromeOptions()
if ambiente_local:
    pass
else:
    chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# setup webdriver with options
if ambiente_local:
    ChromeDriverManager().install()
    driver = webdriver.Chrome(options=chrome_options)
else:
    service = Service(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to Google
driver.get("http://www.google.com")

# Find the title element of the page
title = driver.find_element(By.XPATH, "//title")

# Print the title text
print(title.get_attribute('innerHTML'))

# Close the driver
driver.quit()