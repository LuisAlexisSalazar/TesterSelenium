from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.udemy.com/"
driver.get(url)

# ?open new tab in browser with code javascript
driver.execute_script("window.open('');")

# ?move between tabs
# window_handles: is to identify
driver.switch_to.window(driver.window_handles[1])
driver.get(
    "https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")

# Close a tab[0]
driver.switch_to.window(driver.window_handles[0])
driver.close()
