from selenium.webdriver.common.by import By

from pages.add_employee_page import SAVE_BUTTON
from pages.base_page import BasePage

EMPLOYEE_PROFILE_PICTURE = (By.XPATH, "//div/img[@alt='profile picture']")
INPUT_FILE_LOCATOR = (By.XPATH, "//input[@type='file']")
SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")

class PersonalDetailsPage(BasePage):

    def __init__(self, browser):

        super().__init__(browser)



    def click_profile_picture(self):

            self.click_element(EMPLOYEE_PROFILE_PICTURE)



    def upload_profile_picture(self, file_path):

            self.upload_file(INPUT_FILE_LOCATOR, file_path)



    def click_save_button(self):

            self.click_element(SAVE_BUTTON)