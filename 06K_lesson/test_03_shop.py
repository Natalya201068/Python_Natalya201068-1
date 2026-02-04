import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

url = "https://www.saucedemo.com/"


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


def test_shop(driver):
    wait = WebDriverWait(driver, 10)
    input_name = wait.until(EC.presence_of_element_located(
        (By.ID, 'user-name')))
    input_name.clear()
    input_name.send_keys('standard_user')

    input_password = driver.find_element(By.ID, 'password')
    input_password.clear()
    input_password.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    actions = ActionChains(driver)
    element_1 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    actions.move_to_element(element_1).click().perform()

    element_2 = driver.find_element(
        By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    actions.move_to_element(element_2).click().perform()

    element_3 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie')
    driver.execute_script("arguments[0].scrollIntoView();", element_3)
    actions.move_to_element(element_3).click().perform()

    shopping_cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    driver.execute_script("arguments[0].scrollIntoView();", shopping_cart)
    actions.move_to_element(shopping_cart).click().perform()

    button_checkout = driver.find_element(By.ID, 'checkout')
    driver.execute_script("arguments[0].scrollIntoView();", button_checkout)
    actions.move_to_element(button_checkout).click().perform()

    first_name = driver.find_element(By.ID, 'first-name')
    first_name.clear()
    first_name.send_keys('Natalya')
    last_name = driver.find_element(By.ID, 'last-name')
    last_name.clear()
    last_name.send_keys('Filippova')
    postal_code = driver.find_element(By.ID, 'postal-code')
    postal_code.clear()
    postal_code.send_keys('400067')

    continue_button = driver.find_element(By.ID, 'continue')
    continue_button.click()

    total_label = driver.find_element(By.CLASS_NAME, 'summary_total_label')
    driver.execute_script("arguments[0].scrollIntoView();", total_label)
    total_text = total_label.text

    driver.quit()
    total_amount = f'{total_text}'
    assert total_amount == 'Total: $58.29', f'Сумма {total_text} равна \
        "Total: $58.29"'
