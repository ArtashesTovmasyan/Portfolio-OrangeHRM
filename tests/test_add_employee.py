import time

import allure
from pages.login_page import LoginPage
from pages.side_bar import SideBar

allure.feature("Add Employee")
allure.story("Add Employee")

def test_add_employee(browser):
    allure.severity(allure.severity_level.CRITICAL)
    login_page = LoginPage(browser)
    side_bar = SideBar(browser)
    with allure.step("Open the login page"):
        login_page.open()
    with allure.step("Enter the username and password"):
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
    with allure.step("Click the login button"):
        login_page.click_login_button()
    with allure.step("Click on the PIM side bar item"):
        side_bar.click_on_pim()
