"""
Page Object de la pagina de inventario (listado de productos) de saucedemo.com
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def is_loaded(self) -> bool:
        return self.is_visible(self.PAGE_TITLE) and self.get_text(self.PAGE_TITLE) == "Products"

    def products_count(self) -> int:
        return self.elements_count(self.INVENTORY_ITEMS)

    def add_product_to_cart_by_name(self, product_name: str):
        slug = product_name.lower().replace(" ", "-")
        add_button = (By.ID, f"add-to-cart-{slug}")
        self.click(add_button)

    def add_backpack_to_cart(self):
        self.add_product_to_cart_by_name("Sauce Labs Backpack")

    def remove_backpack_from_cart(self):
        remove_button = (By.ID, "remove-sauce-labs-backpack")
        self.click(remove_button)

    def get_cart_count(self) -> int:
        if not self.is_visible(self.CART_BADGE):
            return 0
        return int(self.get_text(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def sort_products(self, option_value: str):
        """
        Ordena el listado usando el 'value' real del <option> del dropdown
        de saucedemo: 'az', 'za', 'lohi' (precio menor a mayor), 'hilo' (precio mayor a menor).
        """
        from selenium.webdriver.support.ui import Select
        select = Select(self.find(self.SORT_DROPDOWN))
        select.select_by_value(option_value)

    def sort_by_price_low_to_high(self):
        self.sort_products("lohi")

    def sort_by_price_high_to_low(self):
        self.sort_products("hilo")

    def sort_by_name_a_to_z(self):
        self.sort_products("az")

    def sort_by_name_z_to_a(self):
        self.sort_products("za")

    def get_product_prices(self) -> list:
        """Devuelve la lista de precios mostrados, en el orden en que aparecen en pantalla."""
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(e.text.replace("$", "")) for e in price_elements]