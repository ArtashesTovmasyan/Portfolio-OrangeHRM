import time

from pages.login_page import LoginPage
import allure

allure.feature("Login Page")
allure.story("Login")


def test_login(browser):
    allure.severity(allure.severity_level.CRITICAL)
    login_page = LoginPage(browser)
    with allure.step("Open the login page"):
        login_page.open()
    with allure.step("Enter the username and password"):
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
    with allure.step("Click the login button"):
        login_page.click_login_button()
        time.sleep(10)
    with allure.step("Verify the page title"):
        assert login_page.get_page_title() == "OrangeHRM"
