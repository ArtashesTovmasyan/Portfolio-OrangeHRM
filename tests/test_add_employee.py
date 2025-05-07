# tests/test_add_employee.py

import allure
import pytest
from pages.employee_list_page import EmployeeListPage
from pages.pim_page import PimPage

@allure.feature("Employee Management")
@allure.story("Add Employee")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_employee(login, create_employee, cleanup_employee, request):
    employee_id = create_employee
    request.node.employee_id = employee_id  # передаём ID для удаления

    pim_page = PimPage(login)
    employee_list_page = EmployeeListPage(login)

    pim_page.click_employee_list()
    employee_list_page.enter_employee_id(employee_id)
    employee_list_page.click_search_button()

    assert employee_list_page.is_employee_record_present(employee_id), f"Employee {employee_id} not found"

