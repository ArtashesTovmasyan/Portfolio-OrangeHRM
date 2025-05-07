from selenium.webdriver.common.by import By
from pages.base_page import BasePage

LOGIN_INPUT_FIELD = (By.XPATH, "//input[@name = 'username']")
PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@type = 'password']")
LOGIN_BUTTON = (By.XPATH, "//button[@type = 'submit']")


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self, url):
        self.browser.get(url)

    def enter_username(self, username):
        self.enter_text(LOGIN_INPUT_FIELD, username)

    def enter_password(self, password):
        self.enter_text(PASSWORD_INPUT_FIELD, password)

    def click_login_button(self):
        self.click_element(LOGIN_BUTTON)
