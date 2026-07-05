from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_add_product_checkout(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.complete_information("Daiana", "Tester", "1234")

    # Validar que pasaste al step two
    assert "checkout-step-two" in driver.current_url

    checkout.finish_checkout()

    # Validar que el checkout se completó
    assert "checkout-complete" in driver.current_url
    assert "Thank you for your order!" in driver.page_source