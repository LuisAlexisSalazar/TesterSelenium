from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# ?Use xpath when you haven't class,name,id.

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&response_type=html"
driver.get(url)

# ? Xpath Code you can get with ChroPath
# --Relative Path: //input[@id='search']
# --Absolute Path: /html[1]/body[1]/ytd-app[1]/div[1]/div[1]/ytd-masthead[1]/div[3]/div[2]/ytd-searchbox[1]/form[1]/div[1]/div[1]/input[1]
email = driver.find_element(By.XPATH, "//input[@id='email--1']")
email.send_keys("Contraseña")
time.sleep(1)

password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("12345678910")
time.sleep(1)

button = driver.find_element(By.XPATH, "//input[@class='submit']")
button.click()
time.sleep(1)

driver.close()
