import os
import shutil
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage

@pytest.fixture
def browser(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    page = BasePage(driver)  # Create a BasePage instance
    yield page
    time.sleep(5)
    # Take screenshot at the end of the test
    page.take_full_screenshot(f"End_of_{request.node.name}")
    driver.quit()

@pytest.fixture(scope="session")
def employee_id():
    return {"id": None}


def pytest_sessionstart(session):
    allure_results_dir = "./allure-results"
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
        os.makedirs(allure_results_dir, exist_ok=True)