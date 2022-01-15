from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "file:///E:/Repositorio/TesterSelenium/html/promt.html"
driver.get(url)

button = driver.find_element(By.ID, "btn")
button.click()
time.sleep(3)

promt = driver.switch_to.alert
# promt.accept()
promt.dismiss()

# user = input("Ingrese Nombre")
# promt.send_keys(user)
time.sleep(3)

driver.close()
