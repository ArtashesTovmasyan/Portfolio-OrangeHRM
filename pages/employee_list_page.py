from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

EMPLOYEE_ID_FIELD = (By.XPATH, "//label[text()='Employee Id']/../following-sibling::div//input")
SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
RESULT_ROW = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
RECORD_DELETE_BUTTON = (By.XPATH, "//i[@class='oxd-icon bi-trash']")
CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
DELETE_SUCCESS_MESSAGE = (By.XPATH, "//p[contains(normalize-space(), 'Successfully Deleted')]")


class EmployeeListPage(BasePage):
    def enter_employee_id(self, employee_id):
        field = self.find_element(EMPLOYEE_ID_FIELD)
        field.clear()
        field.send_keys(employee_id)

    def click_search_button(self):
        self.click_element(SEARCH_BUTTON)

    def wait_for_search_result(self):
        self.wait.until(EC.presence_of_element_located(RESULT_ROW))

    def wait_for_search_result_or_no_records(self, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                lambda driver: driver.find_elements(*RESULT_ROW) or
                               "No Records Found" in driver.page_source
            )
        except TimeoutException:
            raise Exception("Search results or 'No Records Found' did not appear")

    def is_employee_record_present(self, employee_id):
        self.wait_for_search_result_or_no_records()
        rows = self.browser.find_elements(*RESULT_ROW)
        return any(employee_id in row.text for row in rows)

    def is_employee_record_absent(self, employee_id):
        self.wait_for_search_result_or_no_records()
        rows = self.browser.find_elements(*RESULT_ROW)
        return all(employee_id not in row.text for row in rows)

    def click_on_employee(self, employee_id):
        self.wait_for_search_result_or_no_records()
        rows = self.browser.find_elements(*RESULT_ROW)
        for row in rows:
            if employee_id in row.text:
                row.click()
                break

    def click_delete_button(self):
        self.click_element(RECORD_DELETE_BUTTON)

    def click_yes_delete_button(self):
        self.click_element(CONFIRM_DELETE_BUTTON)

    def is_delete_success_message_present(self):
        return self.is_element_present(DELETE_SUCCESS_MESSAGE)

    def wait_for_delete_success_message(self):
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(DELETE_SUCCESS_MESSAGE)
        )

    def wait_until_employee_disappears(self, employee_id, timeout=10) -> bool:
        try:
            def employee_absent(driver):
                self.wait_for_search_result_or_no_records()
                return not self.is_employee_record_present(employee_id)

            WebDriverWait(self.browser, timeout).until(employee_absent)
            return True
        except TimeoutException:
            return False