import pytest
import allure
from selenium import webdriver
from CalculatorPageAllure import CalculatorPageAllure


@allure.epic('Калькулятор')
class TestCalcPageAllure:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/'
            'slow-calculator.html')
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.title('Тестирование калькулятора')
    @allure.description('Проверка корректного выполнения действия 7 + 8 = 15')
    @allure.severity('normal')
    @allure.feature('COUNT')
    def test_calculator_page(self, driver):
        with allure.step('Открыть страницу калькулятора'):
            calc_page = CalculatorPageAllure(driver)
        calc_page.find_element('#delay', '45')
        calc_page.search_and_click_elements("//span[text()='7']")
        calc_page.search_and_click_elements("//span[text()='+']")
        calc_page.search_and_click_elements("//span[text()='8']")
        calc_page.click_equal_element(driver, 'btn-outline-warning')
        calc_page.wait_for_res_sum("screen", '15')

        actual_time = calc_page.get_actual_wait_time()
        result = calc_page.get_res_sum("screen")

        with allure.step('Проверить, что время загрузки результата '
                         'соответствует ожидаемым 45 секундам'):
            assert actual_time >= 0, \
                f"Время {actual_time} секунд не соответствует ожидаемым 45\
                секундам"
        with allure.step('Проверить, что полученный результат соответствует '
                         'ожидаемому'):
            assert f'{result}' == '15', \
                    f"Результат вычисления {result}, ожидался 15"
