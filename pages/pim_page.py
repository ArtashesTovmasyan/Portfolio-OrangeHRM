from selenium.webdriver.common.by import By
from pages.base_page import BasePage

ADD_BUTTON = (By.XPATH, "//button[text()=' Add ']")


class PimPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_add_button(self):
        self.click_element(ADD_BUTTON)