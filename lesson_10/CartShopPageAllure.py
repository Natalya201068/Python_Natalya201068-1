from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import allure


class CartShopPageAllure:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    @allure.step('Проверить количество товаров в корзине по {locator}')
    def get_cart_items(self, locator) -> list:
        items = self.driver.find_elements(By.CLASS_NAME, locator)
        return items

    @allure.step('Найти кнопку по {locator}, перейти к оформлению покупки')
    def click_checkout(self, locator) -> None:
        button_checkout = self.driver.find_element(By.ID, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   button_checkout)
        self.actions.move_to_element(button_checkout).click().perform()
