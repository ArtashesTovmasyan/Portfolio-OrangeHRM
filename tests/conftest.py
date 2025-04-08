import os
import shutil
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.side_bar import SideBar
from pages.pim_page import PimPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_list_page import EmployeeListPage

@pytest.fixture
def browser(request):
    # initialize chrome driver and maximize window
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    page = BasePage(driver)  # create a basepage instance
    yield page
    time.sleep(5)
    # take screenshot at the end of the test
    page.take_full_screenshot(f"End_of_{request.node.name}")
    driver.quit()

@pytest.fixture
def create_employee(browser):
    """
    Fixture to create an employee.
    Returns the ID of the created employee.
    """
    login_page = LoginPage(browser.browser)
    side_bar = SideBar(browser.browser)
    pim_page = PimPage(browser.browser)
    add_employee_page = AddEmployeePage(browser.browser)

    # login to the system
    login_page.open()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_button()

    # create a new employee
    side_bar.click_on_pim()
    pim_page.click_add_button()
    add_employee_page.enter_first_name("Ben")
    add_employee_page.enter_last_name("Parker")
    add_employee_page.add_employee_id()
    employee_id = add_employee_page.get_employee_id()  # get the employee id
    add_employee_page.click_submit_button()

    # verify successful creation
    assert add_employee_page.is_success_tooltip_displayed(), "The employee was not added successfully"

    yield employee_id  # return the employee id for use in the test

@pytest.fixture
def delete_employee(browser):
    """
    Fixture to delete an employee.
    Takes the employee ID as a parameter and deletes the employee after the test.
    """
    employee_id = yield  # get the employee id from the test

    # delete the employee
    side_bar = SideBar(browser.browser)
    pim_page = PimPage(browser.browser)
    employee_list_page = EmployeeListPage(browser.browser)

    side_bar.click_on_pim()
    pim_page.click_employee_list()
    employee_list_page.enter_employee_id(employee_id)
    employee_list_page.click_search_button()
    employee_list_page.click_delete_button()
    employee_list_page.click_yes_delete_button()

    # verify successful deletion
    assert employee_list_page.is_delete_success_message_present(), "The employee was not deleted successfully"

def pytest_sessionstart(session):
    # clear allure results directory before starting the session
    allure_results_dir = "./allure-results"
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
        os.makedirs(allure_results_dir, exist_ok=True)