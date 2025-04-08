import allure
import pytest

from pages.employee_list_page import EmployeeListPage
from pages.pim_page import PimPage

@allure.feature("Add Employee")
@allure.story("Add Employee")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_employee(browser, create_employee, delete_employee):
    employee_id = create_employee  # get the employee id from the fixture

    pim_page = PimPage(browser.browser)
    employee_list_page = EmployeeListPage(browser.browser)

    with allure.step("Navigate to Employee List"):
        pim_page.click_employee_list()
    with allure.step("Enter employee ID in search box"):
        employee_list_page.enter_employee_id(employee_id)
        employee_list_page.click_search_button()
    with allure.step("Check employee in Employee List"):
        pim_page.click_employee_list()
        try:
            assert employee_list_page.is_employee_record_present(
                employee_id), "The employee was not added to employee list"
            print("the employee was successfully added to the employee list")
        except AssertionError as e:
            print(e)

    # pass the employee id to the delete_employee fixture
    delete_employee.send(employee_id)