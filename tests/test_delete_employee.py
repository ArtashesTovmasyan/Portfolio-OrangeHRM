import allure
import pytest
from pages.employee_list_page import EmployeeListPage
from pages.pim_page import PimPage

@allure.feature("Employee Management")
@allure.story("Delete Employee")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_employee(login, create_employee):
    employee_id = create_employee

    pim_page = PimPage(login)
    employee_list_page = EmployeeListPage(login)

    pim_page.click_employee_list()
    employee_list_page.enter_employee_id(employee_id)
    employee_list_page.click_search_button()
    employee_list_page.click_delete_button()
    employee_list_page.click_yes_delete_button()
    employee_list_page.click_search_button()
    assert employee_list_page.wait_until_employee_disappears(employee_id), f"❗ Employee {employee_id} still exists after deletion"
