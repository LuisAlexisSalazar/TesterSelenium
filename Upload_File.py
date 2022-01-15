from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.w3schools.com/howto/howto_html_file_upload_button.asp"
driver.get(url)

button = driver.find_element(By.ID, "myFile")

button.send_keys("E:\Multimedia\Imagenes\Trabajo\\1626476471622.png")
time.sleep(3)

driver.close()
