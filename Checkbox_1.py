from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.w3schools.com/howto/howto_css_custom_checkbox.asp"
driver.get(url)

# --Selected only one checbox
# checkbox = driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div[1]/input[1]")
checkbox = driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div[1]/input[4]")
print("Is Checkbox Selected? ",checkbox.is_selected())
print("Is Checkbox Enable? ",checkbox.is_enabled())
print("Is Checkbox Displayed? ",checkbox.is_displayed())


#-- Selected second checkbox
checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for check in checkbox:
    if check.is_displayed() is True and check.is_selected() is False:
        check.click()
        time.sleep(3)


driver.close()