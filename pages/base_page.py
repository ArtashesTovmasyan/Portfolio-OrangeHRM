# pages/base_page.py

import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.config import Config

class BasePage:
    def __init__(self, driver):
        self.browser = driver
        self.wait = WebDriverWait(self.browser, 10)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def take_full_screenshot(self, name):
        screenshot_path = os.path.join(Config.screenshot_dir, f"{name}.png")
        self.browser.save_screenshot(screenshot_path)

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
            return True
        except:
            return False

    def upload_file(self, locator, file_path):
        element = self.find_element(locator)
        element.send_keys(file_path)
