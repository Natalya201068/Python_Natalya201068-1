from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class MainShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self, url):
        self.driver.get(url)

    def input_login(self, locator, value):
        input_login = self.driver.find_element(By.ID, locator)
        input_login.clear()
        input_login.send_keys(value)

    def button_click(self, locator):
        login_button = self.driver.find_element(By.ID, locator)
        login_button.click()
