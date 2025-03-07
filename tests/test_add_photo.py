import time

import allure

from pages.employee_list_page import EmployeeListPage
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from pages.side_bar import SideBar
from pages.personal_details_page import PersonalDetailsPage


@allure.feature("Add photo")
@allure.story("Add photo")
@allure.severity(allure.severity_level.NORMAL)
def test_add_photo(browser, employee_id):
    login_page = LoginPage(browser)
    side_bar = SideBar(browser)
    pim_page = PimPage(browser)
    employee_list_page = EmployeeListPage(browser)
    personal_details_page = PersonalDetailsPage(browser)

    with allure.step("login"):
        login_page.open()
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()
    with allure.step("find employee"):
        side_bar.click_on_pim()
        employee_list_page.enter_employee_id(employee_id["id"])
        employee_list_page.click_search_button()
    with allure.step("redirect to personal details page"):
        employee_list_page.click_on_employee(employee_id["id"])
    with allure.step("upload photo"):
        time.sleep(5)
        personal_details_page.click_profile_picture()
        time.sleep(5)
        personal_details_page.upload_profile_picture("C:/Users/atovmasyan/PycharmProjects/PortfolioProject/tests/man-with-beard-avatar-character-isolated-icon-free-vector.jpg")
        personal_details_page.click_save_button()
        time.sleep(15)

