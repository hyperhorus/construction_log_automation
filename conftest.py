import pytest
from utils.driver_factory import get_driver
from utils.config import Config

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()