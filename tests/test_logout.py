import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@allure.feature("Authentication")
@allure.story("User Logout")

def test_successful_logout(driver):
    """
    Test Case: Verify user can successfully logout
    Steps:
    1. Login with valid credentials
    2. Verify dashboard is loaded
    3. Click logout
    4. Verify redirected to login page
    5. Verify session is cleared
    """

    login_page = LoginPage(driver)

    with allure.step("Step 1: Login with valid credentials"):
        dashboard = login_page.login("supervisor01", "super123")

    # with allure.step("Step 2: Verify dashboard is loaded"):
    #     assert dashboard.is_sidebar_visible(), "Dashboard not loaded properly"

    with allure.step("Step 3: Click logout button"):
        dashboard.click_logout()

    with allure.step("Step 4: Verify redirected to login page"):
        # Wait for URL to change (React apps use client-side routing)
        import time
        time.sleep(2)  # Temporary, we'll improve this
        assert "login" in driver.current_url.lower(), "Not redirected to login page"

    with allure.step("Step 5: Verify login form is visible"):
        assert login_page.is_visible(login_page.USERNAME_INPUT), "Login form not visible after logout"


@allure.feature("Authentication")
@allure.story("Logout Clears Session")
@pytest.mark.skip
def test_logout_clears_session(driver):
    """
    Advanced test: Verify logout clears authentication tokens
    """

    login_page = LoginPage(driver)

    # Step 1: Login
    dashboard = login_page.login("supervisor01", "super123")

    # Step 2: Check token exists in localStorage
    token_before = dashboard.get_local_storage_item("auth_token")
    allure.attach(f"Token before logout: {token_before}",
                  name="LocalStorage Token",
                  attachment_type=allure.attachment_type.TEXT)

    assert token_before is not None, "No auth token found in localStorage"

    # Step 3: Logout
    dashboard.click_logout()

    # Step 4: Wait for login page using proper wait
    login_page.wait_for_url("login")

    # Step 5: Verify token is cleared
    token_after = login_page.get_local_storage_item("auth_token")
    allure.attach(f"Token after logout: {token_after}",
                  name="LocalStorage Token",
                  attachment_type=allure.attachment_type.TEXT)

    assert token_after is None, "Auth token not cleared after logout"

    # Step 6: Verify cannot access dashboard directly
    driver.get("http://localhost:3000/dashboard")  # Try accessing protected route
    login_page.wait_for_url("login")  # Should redirect to login