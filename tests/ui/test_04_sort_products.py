from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_sort_products_by_price(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    inventory.sort_by_price_low_to_high()

    prices = inventory.get_product_prices()

    assert prices == sorted(prices)