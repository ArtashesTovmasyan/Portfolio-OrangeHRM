# pages/personal_details_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

PROFILE_PICTURE = (By.XPATH, "//div[@class='orangehrm-edit-employee-image']")
INPUT_FILE_LOCATOR = (By.XPATH, "//input[@type='file']")
SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
TEMP_PHOTO_PREVIEW = (By.XPATH, "//div[contains(@class, 'employee-image-wrapper')]//img")


class PersonalDetailsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.wait = WebDriverWait(browser, 10)

    def click_profile_picture(self):
        self.wait.until(EC.element_to_be_clickable(PROFILE_PICTURE))
        self.click_element(PROFILE_PICTURE)

    def upload_profile_picture(self, file_path):
        element = self.browser.find_element(*INPUT_FILE_LOCATOR)
        element.send_keys(file_path)

    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(SAVE_BUTTON))
        self.click_element(SAVE_BUTTON)

    def is_temp_photo_preview_displayed(self):
        img = self.find_element(TEMP_PHOTO_PREVIEW)
        src = img.get_attribute("src")
        print(f"[DEBUG] Текущий src: {src}")
        return src.startswith("data:image/")

    def get_preview_photo_src(self):
        img = self.find_element((By.XPATH, "//div[contains(@class, 'orangehrm-edit-employee-content')]//img"))
        return img.get_attribute("src")

    def is_preview_photo_changed(self, old_src):
        new_src = self.get_preview_photo_src()
        print(f"[PHOTO SRC] До: {old_src}\nПосле: {new_src}")
        return old_src != new_src
