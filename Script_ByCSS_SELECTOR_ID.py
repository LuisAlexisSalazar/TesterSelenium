from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# ?Syntax for ID and Attribute CSS: tag#id_valor
# Example: input#email--1

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&response_type=html"
driver.get(url)


email = driver.find_element(By.CSS_SELECTOR, "input#email--1")
email.send_keys("Email")
time.sleep(1)

password = driver.find_element(By.CSS_SELECTOR, "input#id_password")
password.send_keys("12345678910")
time.sleep(1)

button = driver.find_element(By.CSS_SELECTOR, "input#submit-id-submit")
button.click()
time.sleep(1)

driver.close()
