from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# ?Use xpath when you haven't class,name,id.

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&response_type=html"
driver.get(url)

# ? ChroPath change CSS Selector for get code
email = driver.find_element(By.CSS_SELECTOR, "input[@id='email--1']")
email.send_keys("Email")
time.sleep(1)

password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
password.send_keys("12345678910")
time.sleep(1)

button = driver.find_element(By.CSS_SELECTOR, "input[name='submit']")
button.click()
time.sleep(1)

driver.close()
