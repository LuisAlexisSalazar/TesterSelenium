from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&response_type=html"
driver.get(url)
time.sleep(1)

# Found by content: return <a></a>
# --Complete value content
# link_recovery_password = driver.find_element(By.LINK_TEXT,"¿Has olvidado la contraseña?")
# --Partical content value
link_recovery_password = driver.find_element(By.PARTIAL_LINK_TEXT, "¿Has")
# print("Element is visible? " + str(link_recovery_password.is_displayed()))
link_recovery_password.click()

# ? Here stay in other tab because do click
email = driver.find_element(By.ID, "form-element--1")
email.send_keys("dfdflujogramas@gmail.com")
time.sleep(1)

# !Part of catch can't automate: Error?
validate = driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border")
validate.click()

button = driver.find_element(By.CLASS_NAME,"btn-primary")
button.click()

driver.close()
