from selenium.webdriver.common.by import By
from pages.base_page import BasePage

EMPLOYEE_ID_INPUT_FIELD = (By.XPATH, "//label[text()='Employee Id']/parent::*/following-sibling::div/input")
SEARCH_BUTTON = (By.XPATH, "//button[text()=' Search ']")
EMPLOYEE_RECORD = (By.XPATH,"//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable' and @role='row']")


class EmployeeListPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def is_employee_record_present(self):
        """Verify that there is exactly one employee record present."""
        records = self.find_elements(EMPLOYEE_RECORD)
        if len(records) != 1:
            raise Exception("Error: There should be exactly one employee record present.")
