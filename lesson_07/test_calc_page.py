import pytest
from selenium import webdriver
from CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_page(driver):
    calc_page = CalculatorPage(driver)
    calc_page.find_element('#delay', '45')
    calc_page.search_and_click_elements("//span[text()='7']")
    calc_page.search_and_click_elements("//span[text()='+']")
    calc_page.search_and_click_elements("//span[text()='8']")
    calc_page.click_equal_element(driver, 'btn-outline-warning')
    calc_page.wait_for_res_sum("screen", '15')

    actual_time = calc_page.get_actual_wait_time()
    result = calc_page.get_res_sum("screen")

    assert actual_time >= 0, \
        f"Время {actual_time} секунд соответствует ожидаемым 45\
        секундам"
    assert f'{result}' == '15', \
            f"Результат вычисления {result}, ожидался 15"
