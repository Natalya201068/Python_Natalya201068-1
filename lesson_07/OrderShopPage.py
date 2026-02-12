from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class OrderShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.total_text = None
        self.total_amount = None
        self.total_txt = None
        self.total = None

    def information(self, locator, value):
        inform = self.driver.find_element(By.ID, locator)
        inform.clear()
        inform.send_keys(value)

    def continue_button(self, locator):
        continue_button = self.driver.find_element(By.ID, locator)
        continue_button.click()

    def get_total_label_order(self, locator):
        total_label = self.driver.find_element(
            By.CLASS_NAME, locator).get_attribute('textContent')

        self.total_txt = total_label
        total_txt = total_label.replace('Total', '').replace(
            ':', '').replace('$', '')
        return float(total_txt)
