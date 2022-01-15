from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.w3schools.com/howto/howto_custom_select.asp"
driver.get(url)

select = driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div[1]/select")

options = select.find_elements(By.TAG_NAME, "option")

for option in options:
    option.click()
    time.sleep(3)

driver.close()
