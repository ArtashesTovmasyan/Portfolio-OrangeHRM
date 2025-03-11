import time

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
from allure_commons.types import AttachmentType
from pages.base_page import BasePage  # Import BasePage

@pytest.fixture
def browser(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    page = BasePage(driver)  # Create a BasePage instance
    yield page # Yield the page object instead of raw driver
    time.sleep(5)
    # Take screenshot at the end of the test
    page.take_full_screenshot(f"End_of_{request.node.name}")
    driver.quit()

@pytest.fixture(scope="session")
def employee_id():
    return {"id": None}