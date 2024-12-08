from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

FIRST_NAME_FIELD = (By.XPATH, "//input[@name='firstName']")
MIDDLE_NAME_FIELD = (By.XPATH, "//input[@name='middleName']")
LAST_NAME_FIELD = (By.XPATH, "//input[@name='lastName']")
EMPLOYEE_ID_FIELD = (By.XPATH, "//div[contains(@class, 'oxd-grid-2')]//input")

SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
CANCEL_BUTTON = (By.XPATH, "//button[text()=' Cancel ']")

SUCCESS_TOOLTIP = (By.XPATH, "//p[text()='Success']")

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddEmployeePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.wait = WebDriverWait(browser, 10)

    def enter_first_name(self, first_name):
        self.wait.until(EC.visibility_of_element_located(FIRST_NAME_FIELD))
        self.enter_text(FIRST_NAME_FIELD, first_name)

    def enter_middle_name(self, middle_name):
        self.wait.until(EC.visibility_of_element_located(MIDDLE_NAME_FIELD))
        self.enter_text(MIDDLE_NAME_FIELD, middle_name)

    def enter_last_name(self, last_name):
        self.wait.until(EC.visibility_of_element_located(LAST_NAME_FIELD))
        self.enter_text(LAST_NAME_FIELD, last_name)

    def enter_employee_id(self, employee_id):
        self.wait.until(EC.visibility_of_element_located(EMPLOYEE_ID_FIELD))
        self.enter_text(EMPLOYEE_ID_FIELD, employee_id)

    def get_employee_id(self):
        self.wait.until(EC.element_to_be_clickable(EMPLOYEE_ID_FIELD))
        element = self.find_element(EMPLOYEE_ID_FIELD)
        element.click()
        element.send_keys(Keys.COMMAND + 'a')  # for windows use Keys.CONTROL
        text = element.get_attribute("value")
        return text

    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(SAVE_BUTTON))
        self.click_element(SAVE_BUTTON)

    def click_cancel_button(self):
        self.wait.until(EC.element_to_be_clickable(CANCEL_BUTTON))
        self.click_element(CANCEL_BUTTON)

    def is_success_tooltip_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(SUCCESS_TOOLTIP))
            return True
        except TimeoutException:
            return False

