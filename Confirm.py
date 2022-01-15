from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "file:///E:/Repositorio/TesterSelenium/html/confirm.html"
driver.get(url)

button = driver.find_element(By.ID, "btn")
button.click()
time.sleep(3)


confirm = driver.switch_to.alert
# https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.alert.html#module-selenium.webdriver.common.alert
# confirm.dismiss() #hide
confirm.accept()
time.sleep(3)

driver.close()