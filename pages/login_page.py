print("LOGIN PAGE CARGADO")

from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver


    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.XPATH, "//h3[@data-test='error']")


    def open(self):
        self.driver.get("https://www.saucedemo.com/")


    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)


    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)


    def click_login(self):
        self.driver.find_element(*self.login_button).click()


    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text