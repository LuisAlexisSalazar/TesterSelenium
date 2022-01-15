from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "file:///E:/Repositorio/TesterSelenium/html/alert.html"
driver.get(url)

button = driver.find_element(By.ID, "btn")
# ?curios when see alert you can't select because it haven't attributes
button.click()
time.sleep(3)

# *Move through alert
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(3)

driver.close()