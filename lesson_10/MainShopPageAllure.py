from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class MainShopPageAllure:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step('Зайти на страницу {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Авторизоваться: найти поле ввода по {locator}, ввести {value}')
    def input_login(self, locator, value) -> None:
        input_login = self.driver.find_element(By.ID, locator)
        input_login.clear()
        input_login.send_keys(value)

    @allure.step('Перейти к списку товаров: найти кнопку по {locator}, кликнуть на нее')
    def button_click(self, locator) -> None:
        login_button = self.driver.find_element(By.ID, locator)
        login_button.click()
