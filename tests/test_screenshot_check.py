import pytest
import allure
from pages.login_page import LoginPage


@allure.feature("Screenshot Demo")
def test_screenshot_on_failure(driver):
    """
    Demo test to show screenshot on failure
    """
    login_page = LoginPage(driver)

    # Take screenshot before failure
    login_page.take_page_screenshot("before_failure")

    # This will fail (intentionally)
    assert 1 == 2, "Intentional failure for screenshot demo"

    # This line won't execute
    login_page.take_page_screenshot("after_failure")


@allure.feature("Screenshot Demo")
def test_element_screenshot(driver):
    """
    Demo element screenshot
    """
    login_page = LoginPage(driver)

    # Take screenshot of username input field
    login_page.take_element_screenshot(
        login_page.USERNAME_INPUT,
        "username_input_field"
    )

    # This should pass
    assert login_page.is_visible(login_page.USERNAME_INPUT)

    # Take success screenshot (with decorator)
    login_page.take_page_screenshot("test_passed")