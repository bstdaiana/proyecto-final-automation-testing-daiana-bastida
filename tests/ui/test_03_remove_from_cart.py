"""
Caso de prueba de UI: eliminar un producto del carrito de saucedemo.com
"""
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_remove_product_from_cart(driver):
    """
    Verifica que al eliminar un producto previamente agregado, el
    contador del carrito vuelva a 0.
    """
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    assert inventory.get_cart_count() == 1

    inventory.remove_backpack_from_cart()
    assert inventory.get_cart_count() == 0