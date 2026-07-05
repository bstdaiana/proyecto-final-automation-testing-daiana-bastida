import json
import pytest

from pages.login_page import LoginPage


def load_users():

    with open("data/users.json") as file:
        return json.load(file)



@pytest.mark.parametrize("user", load_users())
def test_login(driver, user):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        user["username"],
        user["password"]
    )


    if user["type"] == "valid":

        assert "inventory" in driver.current_url


    else:

        assert "Epic sadface" in login_page.get_error_message()