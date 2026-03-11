import os
import allure
from datetime import datetime

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from functools import wraps


class ScreenshotUtils:

    @staticmethod
    def take_screenshot(driver: WebDriver, test_name: str, prefix: str = "failure"):
        """
        Take screenshot and attach to Allure report
        """
        # Clean test name for filename
        safe_test_name = test_name.replace("[", "_").replace("]", "_").replace("/", "_")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = "screenshots"

        # Create directory if it doesn't exist
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # Save screenshot
        filename = f"{prefix}_{safe_test_name}_{timestamp}.png"
        filepath = os.path.join(screenshot_dir, filename)
        driver.save_screenshot(filepath)

        # Attach to Allure report
        allure.attach.file(filepath,
                           name=f"{prefix.capitalize()} Screenshot: {test_name}",
                           attachment_type=allure.attachment_type.PNG)

        return filepath

    @staticmethod
    def take_step_screenshot(driver: WebDriver, step_name: str):
        """
        Take screenshot for a specific step (optional)
        Useful for debugging complex flows
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = "screenshots/steps"

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        filename = f"step_{step_name}_{timestamp}.png"
        filepath = os.path.join(screenshot_dir, filename)
        driver.save_screenshot(filepath)

        allure.attach.file(filepath,
                           name=f"Step: {step_name}",
                           attachment_type=allure.attachment_type.PNG)

    from functools import wraps

    def screenshot_on_failure(func):
        """
        Decorator to add screenshot on test failure
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Find driver in args
                driver = None
                for arg in args:
                    if hasattr(arg, 'save_screenshot'):
                        driver = arg
                        break

                if driver:
                    ScreenshotUtils.take_screenshot(driver, func.__name__, "decorator_failure")

                raise e

        return wrapper

    @pytest.fixture(scope="function", autouse=True)
    def take_screenshot_on_success(request):
        """
        Optional: Take screenshot for every test (successful too)
        Enable with: @pytest.mark.screenshot
        """
        yield

        # Only if test passed and has @pytest.mark.screenshot
        if "screenshot" in request.keywords:
            driver = request.node.funcargs.get('driver')
            if driver and hasattr(request.node, 'rep_call') and request.node.rep_call.passed:
                ScreenshotUtils.take_screenshot(driver, request.node.name, "success")