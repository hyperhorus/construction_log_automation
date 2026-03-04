from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def wait_for_url(self, expected_url_part, timeout=10):
        """
        Wait for URL to contain specific text
        """
        from selenium.webdriver.support import expected_conditions as EC

        def url_contains(driver):
            return expected_url_part in driver.current_url.lower()

        self.wait.until(url_contains)

    def get_local_storage_item(self, key):
        """
        Get item from localStorage (React apps often store tokens here)
        """
        return self.driver.execute_script(f"return localStorage.getItem('{key}');")

    def clear_local_storage(self):
        """
        Clear localStorage
        """
        self.driver.execute_script("window.localStorage.clear();")