import allure
import pytest

from pages.employee_list_page import EmployeeListPage
from pages.pim_page import PimPage

@allure.feature("Delete Employee")
@allure.story("Delete Employee")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_employee(browser, create_employee):
    employee_id = create_employee  # get the employee id from the fixture

    pim_page = PimPage(browser.browser)
    employee_list_page = EmployeeListPage(browser.browser)

    with allure.step("Navigate to PIM and initiate search for employee to delete"):
        pim_page.click_employee_list()
    with allure.step("find employee"):
        employee_list_page.enter_employee_id(employee_id)
        employee_list_page.click_search_button()
    with allure.step("delete employee"):
        employee_list_page.click_delete_button()
        employee_list_page.click_yes_delete_button()
    with allure.step("Verify employee deletion"):
        assert employee_list_page.is_delete_success_message_present(), "The employee was not deleted successfully"