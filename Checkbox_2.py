from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.w3schools.com/howto/howto_css_custom_checkbox.asp"
driver.get(url)

checkbox = driver.find_elements(By.CLASS_NAME, "checkmark")

for check in checkbox:
    if check.is_displayed() is True and check.is_selected() is False:
        check.click()
        time.sleep(3)

driver.close()
