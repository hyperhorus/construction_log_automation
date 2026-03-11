import pytest
import allure
from pages.login_page import LoginPage


# ─────────────────────────────────────────
# Test 1 — Verify Dashboard Loads
# ─────────────────────────────────────────

@allure.feature("Dashboard")
@allure.story("Dashboard loads after login")
def test_dashboard_loads_after_login(driver):
    """
    GIVEN: User is on the login page
    WHEN:  User logs in with valid credentials
    THEN:  Dashboard should load correctly
    """

    login_page = LoginPage(driver)

    with allure.step("Step 1: Login with valid credentials"):
        dashboard = login_page.login("admin", "admin123")

    with allure.step("Step 2: Verify URL changed to dashboard"):
        current_url = dashboard.get_current_url()
        assert "dashboard" in current_url.lower(), \
            f"Expected dashboard URL but got: {current_url}"

    with allure.step("Step 3: Verify dashboard is loaded"):
        assert dashboard.is_dashboard_loaded(), \
            "Dashboard did not load - sidebar not visible"


# ─────────────────────────────────────────
# Test 2 — Verify Navigation Bar Visible
# ─────────────────────────────────────────

@allure.feature("Dashboard")
@allure.story("Navigation bar is visible")
def test_navbar_is_visible(driver):
    """
    GIVEN: User is logged in
    WHEN:  Dashboard loads
    THEN:  Navigation bar should be visible
    """

    login_page = LoginPage(driver)

    with allure.step("Step 1: Login"):
        dashboard = login_page.login("admin", "admin123")

    with allure.step("Step 2: Verify navbar is visible"):
        assert dashboard.is_navbar_visible(), \
            "Navigation bar is not visible on dashboard"


# ─────────────────────────────────────────
# Test 3 — Verify Sidebar is Visible
# ─────────────────────────────────────────

@allure.feature("Dashboard")
@allure.story("Sidebar is visible")
def test_sidebar_is_visible(driver):
    """
    GIVEN: User is logged in
    WHEN:  Dashboard loads
    THEN:  Sidebar should be visible
    """

    login_page = LoginPage(driver)

    with allure.step("Step 1: Login"):
        dashboard = login_page.login("admin", "admin123")

    with allure.step("Step 2: Verify sidebar is visible"):
        assert dashboard.is_sidebar_visible(), \
            "Sidebar is not visible on dashboard"


# ─────────────────────────────────────────
# Test 4 — Verify Correct User is Displayed
# ─────────────────────────────────────────

@allure.feature("Dashboard")
@allure.story("Correct username displayed")
def test_correct_username_displayed(driver):
    """
    GIVEN: User logs in as admin
    WHEN:  Dashboard loads
    THEN:  Admin username should be visible on screen
    """

    login_page = LoginPage(driver)

    with allure.step("Step 1: Login as admin"):
        dashboard = login_page.login("admin", "admin123")

    with allure.step("Step 2: Get displayed username"):
        displayed_name = dashboard.get_logged_in_username()

    with allure.step("Step 3: Verify correct username shown"):
        assert "admin" in displayed_name.lower(), \
            f"Expected admin username but got: {displayed_name}"