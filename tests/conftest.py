# tests/conftest.py

import os
import shutil
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.side_bar import SideBar
from pages.pim_page import PimPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_list_page import EmployeeListPage
from config.config import Config

@pytest.fixture(scope="session")
def browser():
    # Start browser and yield WebDriver instance
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def login(browser):
    # Login before tests
    login_page = LoginPage(browser)
    login_page.open(Config.login_url)
    login_page.enter_username(Config.admin_username)
    login_page.enter_password(Config.admin_password)
    login_page.click_login_button()
    yield browser

@pytest.fixture
def create_employee(login):
    # Create a new employee
    side_bar = SideBar(login)
    pim_page = PimPage(login)
    add_employee_page = AddEmployeePage(login)

    side_bar.click_on_pim()
    pim_page.click_add_button()
    add_employee_page.enter_first_name("Ben")
    add_employee_page.enter_last_name("Parker")
    add_employee_page.add_employee_id()
    employee_id = add_employee_page.get_employee_id()
    add_employee_page.click_submit_button()

    assert add_employee_page.is_success_tooltip_displayed()
    print("Created employee with ID:", employee_id)
    yield employee_id

@pytest.fixture
def cleanup_employee(request, login):
    yield  # Выполняется ПОСЛЕ теста

    employee_id = getattr(request.node, "employee_id", None)
    if not employee_id:
        print("⚠️ No employee ID to cleanup")
        return

    side_bar = SideBar(login)
    pim_page = PimPage(login)
    employee_list_page = EmployeeListPage(login)

    try:
        side_bar.click_on_pim()
        pim_page.click_employee_list()
        employee_list_page.enter_employee_id(employee_id)
        employee_list_page.click_search_button()
        employee_list_page.wait_for_search_result_or_no_records()
        if employee_list_page.is_employee_record_present(employee_id):
            employee_list_page.click_delete_button()
            employee_list_page.click_yes_delete_button()
            employee_list_page.wait_for_delete_success_message()
            employee_list_page.click_search_button()
            employee_list_page.wait_until_employee_disappears(employee_id)
            print(f"Deleted employee with ID: {employee_id}")
        else:
            print(f"Employee ID {employee_id} not found — nothing to delete.")
    except Exception as e:
        print(f"Cleanup failed for employee {employee_id}: {e}")