from selenium.webdriver.common.by import By
from pages.base_page import BasePage

EMPLOYEE_ID_INPUT_FIELD = (By.XPATH, "//label[text()='Employee Id']/parent::*/following-sibling::div/input")
SEARCH_BUTTON = (By.XPATH, "//button[text()=' Search ']")
YES_DELETE_BUTTON = (By.XPATH, "//button[text()=' Yes, Delete ']")
DELETE_SUCCESS_MESSAGE = (By.XPATH, "//p[text()='Successfully Deleted']")
EMPLOYEE_LIST = (By.XPATH, "//a[text()='Employee List']")
RECORD_DELETE_BUTTON = (By.XPATH, "//button/i[@class='oxd-icon bi-trash']")
def employee_recording_id(employee_id):
    return (
    By.XPATH, f"//div[@class='oxd-table-body']//div[contains(@class, 'oxd-table-card')]//div[text()='{employee_id}']")



class EmployeeListPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_employee_list(self):
        self.click_element(EMPLOYEE_LIST)

    def enter_employee_id(self, employee_id):
        self.enter_text(EMPLOYEE_ID_INPUT_FIELD, employee_id)

    def click_search_button(self):
        self.click_element(SEARCH_BUTTON)

    def is_employee_record_present(self, employee_id):
        employee_locator = employee_recording_id(employee_id)
        return self.is_element_present(employee_locator)

    def click_delete_button(self):

        self.click_element(RECORD_DELETE_BUTTON)

    def find_employee_by_id(self, employee_id):
        employee_locator = employee_recording_id(employee_id)
        return self.find_element(employee_locator)

    def click_yes_delete_button(self):
        self.click_element(YES_DELETE_BUTTON)

    def is_delete_success_message_present(self):
        return self.is_element_present(DELETE_SUCCESS_MESSAGE)



    def click_on_employee(self, employee_id):
        employee_locator = employee_recording_id(employee_id)
        self.click_element(employee_locator)