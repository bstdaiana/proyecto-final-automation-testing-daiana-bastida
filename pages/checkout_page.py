from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")

    def complete_information(self, first, last, postal):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(postal)
        # Paso clave: avanzar al step two
        self.driver.find_element(*self.continue_button).click()

    def finish_checkout(self):
        # Esperar hasta que el botón Finish esté disponible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.finish_button)
        )
        self.driver.find_element(*self.finish_button).click()
