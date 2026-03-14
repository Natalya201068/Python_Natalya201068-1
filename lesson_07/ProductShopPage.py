from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProductShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def add_products(self, locator):
        product = self.driver.find_element(By.ID, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", product)
        self.actions.move_to_element(product).click().perform()

    def go_to_cart(self, locator):

        shopping_cart = self.driver.find_element(By.CLASS_NAME,
                                                 locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   shopping_cart)
        self.actions.move_to_element(shopping_cart).click().perform()
