from selenium.webdriver.common.by import By
from pages.base_page import BasePage

FIRST_NAME_FIELD = (By.XPATH, "//input[@name='firstName']")
MIDDLE_NAME_FIELD = (By.XPATH, "//input[@name='middleName']")
LAST_NAME_FIELD = (By.XPATH, "//input[@name='lastName']")
EMPLOYEE_ID_FIELD = (By.XPATH, "//div[contains(@class, 'oxd-grid-2')]//input")

SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
CANCEL_BUTTON = (By.XPATH, "//button[text()=' Cancel ']")


class AddEmployeePage(BasePage):
    def __init__(self):
        super().__init__()

    def enter_first_name(self, first_name):
        self.enter_text(FIRST_NAME_FIELD, first_name)

    def enter_middle_name(self, middle_name):
        self.enter_text(MIDDLE_NAME_FIELD, middle_name)

    def enter_last_name(self, last_name):
        self.enter_text(LAST_NAME_FIELD, last_name)

    def enter_employee_id(self, employee_id):
        self.enter_text(EMPLOYEE_ID_FIELD, employee_id)

    def click_submit_button(self):
        self.click_element(SAVE_BUTTON)

    def click_cancel_button(self):
        self.click_element(CANCEL_BUTTON)

    

