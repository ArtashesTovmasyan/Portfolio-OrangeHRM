import time

from pages.personal_details_page import PersonalDetailsPage
from pages.login_page import LoginPage
from pages.employee_list_page import EmployeeListPage
from pages.pim_page import PimPage
import allure

from pages.side_bar import SideBar
from tests.conftest import employee_id

employee_id = "046711941a"
@allure.feature("Personal Details")
@allure.story("Add Photo")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_photo(browser):
    personal_details_page = PersonalDetailsPage(browser)
    login_page = LoginPage(browser)
    employee_list_page = EmployeeListPage(browser)
    pim_page = PimPage(browser)
    side_bar = SideBar(browser)

    with allure.step("Open the login page"):
        login_page.open()
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()
    with allure.step("Navigate to Employee List"):
        side_bar.click_on_pim()
    with allure.step("Select an employee"):
        employee_list_page.enter_employee_id(employee_id)
        employee_list_page.click_search_button()
        employee_list_page.click_on_employee(employee_id)
        time.sleep(5)

    with allure.step("click on the photo"):
        personal_details_page.click_profile_picture()
    with allure.step("Upload a photo"):
        personal_details_page.upload_profile_picture("man-with-beard-avatar-character-isolated-icon-free-vector.jpg")
        personal_details_page.click_save_button()