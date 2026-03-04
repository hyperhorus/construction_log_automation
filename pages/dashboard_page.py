from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):

    # Update these selectors based on your actual app
    USER_MENU = (By.XPATH, "//div/button/div")  # if dropdown
    LOGOUT_OPTION = (By.XPATH, "//li[text()='Logout']")
    DASHBOARD_TITLE = (By.TAG_NAME, "h1")
    SIDEBAR = (By.CLASS_NAME, "sidebar")

    def click_logout(self):
        # Handle dropdown logout
        if self.is_visible(self.USER_MENU):
            self.click(self.USER_MENU)
            self.click(self.LOGOUT_OPTION)
        else:
            self.click(self.LOGOUT_BUTTON)

    def get_welcome_message(self):
        return self.get_text(self.DASHBOARD_TITLE)

    # def is_sidebar_visible(self):
    #     return self.is_visible(self.SIDEBAR)