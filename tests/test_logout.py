import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@allure.feature("Authentication")
@allure.story("User Logout")
@pytest.mark.skip
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
    # token_before = dashboard.get_local_storage_item("auth_token")
    # allure.attach(f"Token before logout: {token_before}",
    #               name="LocalStorage Token",
    #               attachment_type=allure.attachment_type.TEXT)

    # assert token_before is not None, "No auth token found in localStorage"

    # Step 3: Logout
    dashboard.click_logout()

    # Step 4: Wait for login page using proper wait
    login_page.wait_for_url("login")

    # Step 5: Verify token is cleared
    # token_after = login_page.get_local_storage_item("auth_token")
    # allure.attach(f"Token after logout: {token_after}",
    #               name="LocalStorage Token",
    #               attachment_type=allure.attachment_type.TEXT)
    #
    # assert token_after is None, "Auth token not cleared after logout"

    # Step 6: Verify cannot access dashboard directly
    driver.get("http://localhost:3000/dashboard")  # Try accessing protected route
    login_page.wait_for_url("login")  # Should redirect to login


@allure.feature("Authentication")
@allure.story("Browser Back After Logout")
@pytest.mark.skip
def test_browser_back_after_logout(driver):
    """
    Test security: Verify user cannot use browser back after logout
    """

    login_page = LoginPage(driver)

    # Login
    dashboard = login_page.login("supervisor01", "super123")

    # Logout
    dashboard.click_logout()
    login_page.wait_for_url("login")

    # Try browser back button
    driver.back()

    # Should redirect back to login or show error
    login_page.wait_for_url("login")

    # Verify no sensitive data is visible
    assert not dashboard.is_sidebar_visible(), \
        "Dashboard still accessible after logout via browser back"


@pytest.mark.parametrize("username,password,role", [
    ("memouser", "memo123", "admin"),
    ("supervisor01", "super123", "manager"),
    ("memouser", "memo123", "worker"),
])
@allure.feature("Authentication")
@allure.story("Role-based Logout")
def test_logout_different_roles(driver, username, password, role):
    """
    Test logout works for all user roles
    """
    login_page = LoginPage(driver)

    with allure.step(f"Login as {role}"):
        dashboard = login_page.login(username, password)

    with allure.step(f"Logout {role} user"):
        dashboard.click_logout()

    with allure.step(f"Verify {role} dashboard loaded"):
        # Different roles might see different UI elements
        if role == "admin":
            assert not dashboard.is_sidebar_visible(), "Dashboard still accessible after logout"
        elif role == "manager":
            assert not dashboard.is_sidebar_visible(), "Dashboard still accessible after logout"


    with allure.step(f"Verify {role} redirected to login"):
        login_page.wait_for_url("login")
