import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage

class LoginPage(BasePage):

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".MuiAlert-message.css-zioonp-MuiAlert-message")  # adjust if needed


    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        time.sleep(2)
        return DashboardPage(self.driver)  # Return dashboard page object


    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)