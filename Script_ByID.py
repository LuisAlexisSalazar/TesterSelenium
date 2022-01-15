from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# url = "https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F"
url = "https://www.youtube.com/"
driver.get(url)
# driver.maximize_window()
time.sleep(1)

# !find_element_by_id is deprecated, use find_element or find_elements
email = driver.find_element(By.ID, "search-form")
print("Element is visible? " + str(email.is_displayed()))
time.sleep(1)

email = email.find_element(By.ID, "search")
email.send_keys("Contenido de tu gusto")
time.sleep(1)

button_log_in = driver.find_element(By.ID, "search-icon-legacy")
button_log_in.click()

time.sleep(5)

# Difference: https://www.tutorialspoint.com/state-the-differences-between-close-and-quit
# driver.quit() #close all tab
driver.close()  #close 1 tab
