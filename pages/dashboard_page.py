from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    # Update these selectors based on your actual app
    USER_MENU = (By.XPATH, "//div/button/div")  # if dropdown
    LOGOUT_OPTION = (By.XPATH, "//li[text()='Logout']")
    DASHBOARD_TITLE = (By.TAG_NAME, "h1")
    SIDEBAR = (By.XPATH, "//header")
    DASHBOARD = (By.XPATH, "//a[normalize-space()='Dashboard']")
    PROJECTS = (By.XPATH, "//a[normalize-space()='Projects']")
    ISSUES = (By.XPATH, "//a[normalize-space()='Issues']")
    DOCUMENTS = (By.XPATH, "//a[normalize-space()='Documents']")
    DAILY_LOGS = (By.XPATH, "//a[normalize-space()='Daily Logs']")
    MORE_BUTTON = (By.XPATH, "//button[normalize-space()='More']")
    EQUIPMENT = (By.XPATH, "//span[normalize-space()='Equipment']")
    MATERIAL = (By.XPATH, "//span[text()='Materials']")
    INSPECTIONS = (By.XPATH, "//span[text()='Inspections']")
    SUBCONTRACTORS = (By.XPATH, "//span[text()='Subcontractors']")
    PHOTOS = (By.XPATH, "//span[text()='Photos']")
    TIME_TRACKING = (By.XPATH, "//span[text()='Time Tracking']")
    SAFETY_INCIDENTS = (By.XPATH, "//span[text()='Safety incidents']")
    REPORTS = (By.XPATH, "//span[text()='Reports']")
    USER_NAME_DISPLAY = (By.XPATH, "//div/p[contains(text(),'usuario')]")
    WORKERS = (By.XPATH, "//div[contains(text(),'workers')]")

    def click_logout(self):
        # Handle dropdown logout
        if self.is_visible(self.USER_MENU):
            self.click(self.USER_MENU)
            self.click(self.LOGOUT_OPTION)
        else:
            self.click(self.LOGOUT_BUTTON)

    def get_welcome_message(self):
        return self.get_text(self.DASHBOARD_TITLE)

    def is_sidebar_visible(self):
        print(f"valor del sidebar{self.is_visible(self.SIDEBAR)}")
        return self.is_visible(self.SIDEBAR)

    def is_dashboard_visible(self):
        return self.is_visible(self.DASHBOARD)

    def is_project_visible(self):
        return self.is_visible(self.PROJECTS)

    def is_equipment_visible(self):
        return self.is_visible(self.EQUIPMENT)

    def is_material_visible(self):
        return self.is_visible(self.MATERIAL)

    def is_inspections_visible(self):
        return self.is_visible(self.INSPECTIONS)

    def is_subcontracts_visible(self):
        return self.is_visible(self.SUBCONTRACTORS)

    def is_photos_visible(self):
        return self.is_visible(self.PHOTOS)

    def is_time_tracking_visible(self):
        return self.is_visible(self.TIME_TRACKING)

    def is_safety_incidents_visible(self):
        return self.is_visible(self.SAFETY_INCIDENTS)

    def is_report_visible(self):
        return self.is_visible(self.REPORTS)

    def is_worker_visible(self):
        return self.is_visible(self.WORKERS)

    def is_more_visible(self):
        return self.is_visible(self.MORE_BUTTON)

    def get_logged_in_username(self):
        """
        Get the username displayed on the dashboard
        """
        return self.get_text(self.USER_NAME_DISPLAY)

    def navigate_to_projects(self):
        """
        Click Projects in the navigation menu
        """
        self.click(self.PROJECTS)

    def navigate_to_daily_logs(self):
        """
        Click Daily Logs in the navigation menu
        """
        self.click(self.DAILY_LOGS)

    def navigate_to_equipment(self):
        self.click(self.MORE_BUTTON)
        self.click(self.EQUIPMENT)

    def navigate_to_materials(self):
        self.click(self.MORE_BUTTON)
        self.click(self.MATERIAL)

    def navigate_to_inspections(self):
        self.click(self.MORE_BUTTON)
        self.click(self.INSPECTIONS)

    def navigate_to_subcontractors(self):
        self.click(self.MORE_BUTTON)
        self.click(self.SUBCONTRACTORS)

    def navigate_to_photos(self):
        self.click(self.MORE_BUTTON)
        self.click(self.PHOTOS)

    def navigate_to_time_tracking(self):
        self.click(self.MORE_BUTTON)
        self.click(self.TIME_TRACKING)

    def navigate_to_safety_incidents(self):
        self.click(self.MORE_BUTTON)
        self.click(self.SAFETY_INCIDENTS)

    def navigate_to_reports(self):
        self.click(self.MORE_BUTTON)
        self.click(self.REPORTS)

    def navigate_to_workers(self):
        """
        Click Workers in the navigation menu
        """
        self.click(self.MORE_BUTTON)
        self.click(self.WORKERS)

    def get_current_url(self):
        """
        Return the current browser URL
        """
        return self.driver.current_url

    def logout(self):
        """
        Click the logout button.
        Returns LoginPage after logout.
        """
        from pages.login_page import LoginPage
        self.click(self.LOGOUT_BUTTON)
        return LoginPage(self.driver)
