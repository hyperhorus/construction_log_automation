import pytest
from utils.driver_factory import get_driver
from utils.config import Config
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_user(driver):
    login_page = LoginPage(driver)
    login_page.login("supervisor01", "super123")
    return driver