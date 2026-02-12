from typing import AnyStr
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = [None]
        self.wait = WebDriverWait(driver, 50)
        self.actions = ActionChains(driver)
        self.actual_wait_time = None
        self.screen_element = None
        self.res_sum = AnyStr
        self.start_time = None
        self.end_time = None

    def find_element(self, locator, value):
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        element.clear()
        element.send_keys(value)

    def search_and_click_elements(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()

    def click_equal_element(self, driver, locator):
        equal_element = self.driver.find_element(By.CLASS_NAME,
                                                 locator)
        actions = ActionChains(driver)
        actions.move_to_element(equal_element).click().perform()

    def wait_for_res_sum(self, locator, res):
        self.start_time = time.time()

        self.wait.until(
            EC.visibility_of_element_located((By.ID, 'spinner')))

        screen_element = self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, locator), text_=res))
        return screen_element

    def get_actual_wait_time(self):
        self.end_time = time.time()
        self.actual_wait_time = self.end_time - self.start_time
        return self.actual_wait_time

    def get_res_sum(self, locator):

        res_sum = self.driver.find_element(By.CLASS_NAME, locator)
        result = res_sum.get_attribute('textContent')
        return result
