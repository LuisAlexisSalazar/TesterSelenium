from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Back between tabs
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.google.com.pr/"
driver.get(url)
time.sleep(3)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(url)
time.sleep(3)
url = "https://www.facebook.com/"
driver.get(url)
time.sleep(3)

url = "https://www.google.com.pr/"
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get(url)
time.sleep(3)
url = "https://www.youtube.com/"
driver.get(url)
time.sleep(3)
driver.back()
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
driver.back()
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
driver.close()
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
driver.close()
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
driver.forward()
time.sleep(3)

driver.quit()