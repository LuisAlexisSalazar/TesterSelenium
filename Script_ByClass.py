from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.youtube.com/"
driver.get(url)

email = driver.find_element(By.CLASS_NAME, "style-scope ytd-searchbox")
print("Element is visible? " + str(email.is_displayed()))

button_log_in = driver.find_element(By.ID, "search-icon-legacy")
email.send_keys("Contenido de tu gusto por Class Name")
time.sleep(3)

driver.close()