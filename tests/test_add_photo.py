import allure
import pytest

from pages.employee_list_page import EmployeeListPage
from pages.personal_details_page import PersonalDetailsPage
from pages.pim_page import PimPage

@allure.feature("Add photo")
@allure.story("Add photo")
@allure.severity(allure.severity_level.NORMAL)
def test_add_photo(browser, create_employee, delete_employee):
    employee_id = create_employee  # get the employee id from the fixture

    pim_page = PimPage(browser.browser)
    employee_list_page = EmployeeListPage(browser.browser)
    personal_details_page = PersonalDetailsPage(browser.browser)

    with allure.step("find employee"):
        pim_page.click_employee_list()
        employee_list_page.enter_employee_id(employee_id)
        employee_list_page.click_search_button()
    with allure.step("redirect to personal details page"):
        employee_list_page.click_on_employee(employee_id)
    with allure.step("upload photo"):
        personal_details_page.click_profile_picture()
        personal_details_page.upload_profile_picture(
            "C:/Users/atovmasyan/PycharmProjects/PortfolioProject/tests/man-with-beard-avatar-character-isolated-icon-free-vector.jpg")
        personal_details_page.click_save_button()

    # pass the employee id to the delete_employee fixture
    delete_employee.send(employee_id)