"""
BasePage: clase padre de todas las Page Objects.
Concentra los metodos de interaccion genericos (esperas, clicks, envio de
texto, lectura de texto) para que las paginas hijas no repitan codigo
boilerplate de Selenium.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self, url: str):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.find_clickable(locator).click()

    def type_text(self, locator, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        return self.find(locator).text

    def is_visible(self, locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def elements_count(self, locator) -> int:
        return len(self.driver.find_elements(*locator))