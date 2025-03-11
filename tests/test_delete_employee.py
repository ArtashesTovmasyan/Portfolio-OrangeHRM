import time
import allure

from pages.employee_list_page import EmployeeListPage
from pages.pim_page import PimPage
from pages.login_page import LoginPage
from pages.side_bar import SideBar
from pages.add_employee_page import AddEmployeePage, employee_id_generator


@allure.feature("Delete Employee")
@allure.story("Delete Employee")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_employee(browser, employee_id):
    login_page = LoginPage(browser.browser)
    side_bar = SideBar(browser.browser)
    pim_page = PimPage(browser.browser)
    add_employee_page = AddEmployeePage(browser.browser)
    employee_list_page = EmployeeListPage(browser.browser)

    with allure.step("Open the login page"):
        login_page.open()
    with allure.step("Enter credentials and login"):
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()
    with allure.step("Navigate to PIM and initiate search for employee to delete"):
        side_bar.click_on_pim()
    with allure.step("find employee"):
        employee_list_page.enter_employee_id(employee_id["id"])
        employee_list_page.click_search_button()
    with allure.step("delete employee"):
        employee_list_page.click_delete_button()
        employee_list_page.click_yes_delete_button()
    with allure.step("Verify employee deletion"):
        assert employee_list_page.is_delete_success_message_present(), "The employee was not deleted successfully"
