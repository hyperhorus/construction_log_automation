import pytest
import os
from datetime import datetime
from utils.driver_factory import get_driver
from utils.config import Config
from pages.login_page import LoginPage
import allure

@pytest.fixture(scope="function")
def driver(request):
    """
    Enhanced driver fixture with:
    1. Automatic screenshot on failure
    2. Test name tracking
    3. Browser log capture
    """
    driver = get_driver()
    driver.test_name = request.node.name  # Store test name on driver
    driver.get(Config.BASE_URL)

    yield driver

    # After test completes
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Step 1: Run the test and get the result
    outcome = yield
    report = outcome.get_result()

    # Step 2: Check if it was the actual test that failed
    # (not the setup or teardown)
    if report.when == "call" and report.failed:

        # Step 3: Get the driver from the test
        driver = item.funcargs.get("driver")

        # Step 4: Only take screenshot if driver exists
        if driver:

            # Step 5: Create a timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Step 6: Create screenshots folder if it doesn't exist
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            # Step 7: Build the screenshot file name
            test_name = item.name
            screenshot_name = f"{test_name}_{timestamp}.png"
            screenshot_path = os.path.join("screenshots", screenshot_name)

            # Step 8: Take the screenshot and save it
            driver.save_screenshot(screenshot_path)

            # Step 9: Print confirmation in terminal
            print(f"\n📸 Screenshot saved: {screenshot_path}")

            # Attach to Allure report ← ADD THESE 4 LINES
            with open(screenshot_path, "rb") as image_file:
                allure.attach(
                    image_file.read(),
                    name=f"FAILED - {test_name}",
                    attachment_type=allure.attachment_type.PNG
                )

@pytest.fixture
def logged_in_user(driver):
    login_page = LoginPage(driver)
    login_page.login("supervisor01", "super123")
    return driver