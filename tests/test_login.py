import pytest
import allure
from pages.login_page import LoginPage

@allure.feature("Login")
@allure.story("Valid Login")
@pytest.mark.skip
def test_valid_login(driver):

    login_page = LoginPage(driver)

    with allure.step("Enter valid credentials"):
        login_page.login("supervisor01", "super123")

    with allure.step("Verify login successful"):
        #assert "dashboard" in driver.current_url.lower()
        assert "http://localhost:3000/" in driver.current_url

@allure.feature("Login")
@allure.story("Invalid Login")
#@pytest.mark.skip
def test_invalid_login(driver):

    login_page = LoginPage(driver)

    with allure.step("Enter invalid credentials"):
        login_page.login("wronguser", "wrongpass")

    with allure.step("Verify error message displayed"):
        assert login_page.is_visible(login_page.ERROR_MESSAGE)
