from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
# !New class to tag Select : https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.select
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.w3schools.com/howto/howto_custom_select.asp"
driver.get(url)

select = Select(driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div[1]/select"))
time.sleep(3)

# ?Index
select.select_by_index(11)
time.sleep(3)

# ? Select a option (Jaguar) with value 6 by page
select.select_by_value("6")
time.sleep(3)

# ?Value of tag
select.select_by_visible_text("Ford")
time.sleep(3)

driver.close()
