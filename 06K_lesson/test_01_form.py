import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

key = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'zip-code',
       'city', 'country', 'job-position', 'company']
value = ['Иван', 'Петров', 'Ленина, 55-3', 'test@skypro.com',
         '+7985899998787', '', 'Москва', 'Россия', 'QA', 'SkyPro']
test_data = dict(zip(key, value))

url = 'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'


@pytest.fixture(scope="function")
def browser():
    driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    driver_instance.get(url)
    yield driver_instance
    driver_instance.quit()


def test_form_validation_complete(browser):

    for i in range(0, len(test_data)):
        input_key = browser.find_element(By.NAME, key[i])
        input_key.clear()
        input_key.send_keys(value[i])

    element = browser.find_element(By.CLASS_NAME, 'btn-outline-primary')
    actions = ActionChains(browser)
    actions.move_to_element(element).click().perform()

    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert"))
    )
    for i in range(0, len(test_data)):
        field = browser.find_element(By.ID, key[i])
        if i == 5:
            assert 'alert-danger' in field.get_attribute("class"), \
                "✓ Поле 'zip-code' подсвечено красным"
        else:
            assert 'alert-success' in field.get_attribute("class"), \
                f"✓ Поле '{key[i]}' подсвечено зеленым"
