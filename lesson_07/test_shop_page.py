import pytest
from MainShopPage import MainShopPage
from ProductShopPage import ProductShopPage
from CartShopPage import CartShopPage
from OrderShopPage import OrderShopPage
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_page(driver):
    shop_page = MainShopPage(driver)
    shop_page.open('https://www.saucedemo.com/')
    shop_page.input_login('user-name', "standard_user")
    shop_page.input_login('password', "secret_sauce")
    shop_page.button_click('login-button')

    product = ProductShopPage(driver)
    product.add_products('add-to-cart-sauce-labs-backpack')
    product.add_products('add-to-cart-sauce-labs-bolt-t-shirt')
    product.add_products('add-to-cart-sauce-labs-onesie')
    product.go_to_cart('shopping_cart_link')

    cart_element = CartShopPage(driver)
    items = cart_element.get_cart_items('cart_item')
    cart_element.click_checkout('checkout')

    order = OrderShopPage(driver)
    order.information('first-name', "Natalya")
    order.information('last-name', "Filippova")
    order.information('postal-code', "400067")
    order.continue_button('continue')
    total_txt = order.get_total_label_order('summary_total_label')

    assert len(items) == 3, f"В корзине должно быть 3 товара, а там {len(items)}"

    total_amount = f'Total: ${total_txt}'
    assert total_amount == 'Total: $58.29', f'Сумма ${total_txt} равна \
        $58.29'
