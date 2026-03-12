import pytest
from MainShopPageAllure import MainShopPageAllure
from ProductShopPageAllure import ProductShopPageAllure
from CartShopPageAllure import CartShopPageAllure
from OrderShopPageAllure import OrderShopPageAllure
from selenium import webdriver
import allure


@allure.epic('Онлайн-магазин')
class TestShopPageAllure:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.title('Тестирование покупки')
    @allure.description('Выбор и оформление покупки товаров '
                        'в онлайн-магазине')
    @allure.severity('blocker')
    @allure.feature('PURCHASE')
    def test_shop_page(self, driver):
        shop_page = MainShopPageAllure(driver)
        with allure.step('Открыть страницу магазина'):
            shop_page.open('https://www.saucedemo.com/')
        shop_page.input_login('user-name', "standard_user")
        shop_page.input_login('password', "secret_sauce")
        shop_page.button_click('login-button')

        product = ProductShopPageAllure(driver)
        product.add_products('add-to-cart-sauce-labs-backpack')
        product.add_products('add-to-cart-sauce-labs-bolt-t-shirt')
        product.add_products('add-to-cart-sauce-labs-onesie')
        product.go_to_cart('shopping_cart_link')

        cart_element = CartShopPageAllure(driver)
        items = cart_element.get_cart_items('cart_item')
        cart_element.click_checkout('checkout')

        order = OrderShopPageAllure(driver)
        order.information('first-name', "Natalya")
        order.information('last-name', "Philippo")
        order.information('postal-code', "400067")
        order.continue_button('continue')
        total_txt = order.get_total_label_order('summary_total_label')

        with allure.step('Проверить, что в корзине 3 товара'):
            assert len(items) == 3, (f"В корзине должно быть 3 товара, "
                                     f"а там {len(items)}")

        total_amount = f'Total: ${total_txt}'
        with allure.step('Проверить, что итоговая сумма равна $58.29'):
            assert total_amount == 'Total: $58.29', (f'Сумма ${total_txt} '
                                                     f'равна $58.29')
