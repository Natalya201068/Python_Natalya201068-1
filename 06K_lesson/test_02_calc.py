import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


url = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'


@pytest.fixture(scope="function")
def browser():
    driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    driver_instance.get(url)
    yield driver_instance
    driver_instance.quit()


def test_find_element_and_time(browser):
    element = browser.find_element(By.CSS_SELECTOR, '#delay')
    element.clear()
    element.send_keys('45')

    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    element = browser.find_element(By.CLASS_NAME, 'btn-outline-warning')
    actions = ActionChains(browser)
    actions.move_to_element(element).click().perform()

    start_time = time.time()

    EC.presence_of_element_located((By.CLASS_NAME, "spinner"))

    WebDriverWait(browser, 50).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "screen")))

    end_time = time.time()
    actual_wait_time = end_time - start_time

    assert abs(45 - actual_wait_time) >= 0, \
        f"Время {actual_wait_time} секунд соответствует ожидаемым 45\
        секундам"
