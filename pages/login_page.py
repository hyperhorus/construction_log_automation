import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage

class LoginPage(BasePage):

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".MuiAlert-message.css-zioonp-MuiAlert-message")  # adjust if needed

    def wait_for_url(self, expected_url_part, timeout=10):
        """
        Wait for URL to contain specific text
        """
        from selenium.webdriver.support import expected_conditions as EC

        def url_contains(driver):
            return expected_url_part in driver.current_url.lower()

        self.wait.until(url_contains)

    def login(self, username, password):
        from pages.dashboard_page import DashboardPage

        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        time.sleep(2)
        return DashboardPage(self.driver)  # Return dashboard page object


    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)