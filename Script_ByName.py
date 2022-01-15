from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.youtube.com/"
driver.get(url)

email = driver.find_element(By.ID, "search-form")
print("Element is visible? " + str(email.is_displayed()))

email = email.find_element(By.NAME, "search_query")
email.send_keys("Contenido de tu gusto por Name")
time.sleep(3)

driver.close()