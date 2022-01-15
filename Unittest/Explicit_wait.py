import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# !New class to take time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpCon


class class_unit_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_usando_Explicit_wait(self):
        url = "https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&response_type=html"
        self.driver.get(url)

        try:
            # ? Espera por 10 segundos hasta que se haga presente el emento email
            element = WebDriverWait(self.driver, 10).until(ExpCon.presence_of_element_located((By.NAME, "email")))
        finally:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()


