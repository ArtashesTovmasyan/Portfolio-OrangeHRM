import time
import allure


from pages.employee_list_page import EmployeeListPage
from pages.pim_page import PimPage
from pages.login_page import LoginPage
from pages.side_bar import SideBar
from pages.add_employee_page import AddEmployeePage, employee_id_generator




@allure.feature("Add Employee")
@allure.story("Add Employee")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_employee(browser, employee_id):
    login_page = LoginPage(browser)
    side_bar = SideBar(browser)
    pim_page = PimPage(browser)
    add_employee_page = AddEmployeePage(browser)
    employee_list_page = EmployeeListPage(browser)

    with allure.step("Open the login page"):
        login_page.open()
    with allure.step("Enter credentials and login"):
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()
    with allure.step("Navigate to PIM and initiate adding a new employee"):
        side_bar.click_on_pim()
        pim_page.click_add_button()
    with allure.step("Enter employee details"):
        add_employee_page.enter_first_name("Ben")
        add_employee_page.enter_last_name("Parker")
        add_employee_page.add_employee_id()
        employee_id["id"] = add_employee_page.get_employee_id()  # Employee ID for verification
    with allure.step("Submit new employee details"):
        add_employee_page.click_submit_button()
    with allure.step("Verify employee creation"):
        assert add_employee_page.is_success_tooltip_displayed(), "The employee was not added successfully"
    with allure.step("Navigate to Employee List"):
        pim_page.click_employee_list()
    with allure.step("Enter employee ID in search box"):
        employee_list_page.enter_employee_id(employee_id["id"])
        time.sleep(5)
        employee_list_page.click_search_button()
        time.sleep(5)
    with allure.step("Check employee in Employee List"):
        pim_page.click_employee_list()
        try:
            assert employee_list_page.is_employee_record_present(employee_id["id"]), "The employee was not added to employee list"
            print("The employee was successfully added to the employee list")
        except AssertionError as e:
            print(e)





@allure.feature("Delete Employee")
@allure.story("Delete Employee")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_employee(browser, employee_id):
    login_page = LoginPage(browser)
    side_bar = SideBar(browser)
    pim_page = PimPage(browser)
    add_employee_page = AddEmployeePage(browser)
    employee_list_page = EmployeeListPage(browser)

    with allure.step("Open the login page"):
        login_page.open()
    with allure.step("Enter credentials and login"):
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()
    with allure.step("Navigate to PIM and initiate search for employee to delete"):
        side_bar.click_on_pim()
    with allure.step("Enter employee ID in search box"):
        employee_list_page.enter_employee_id("044049412a")
        employee_list_page.click_search_button()
    with allure.step("find employee and delete"):
        employee_list_page.click_delete_button()
        employee_list_page.click_yes_delete_button()
    with allure.step("Verify employee deletion"):
        assert  employee_list_page.is_delete_success_message_present(), "The employee was not deleted successfully"
