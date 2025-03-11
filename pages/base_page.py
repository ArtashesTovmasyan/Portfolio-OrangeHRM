# pages/base_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    main_url = "https://opensource-demo.orangehrmlive.com/web/index.php/"

    def open(self, url=None):
        # Open the specified URL or the main_url if none provided
        url = url or self.main_url
        self.browser.get(url)

    def find_element(self, locator):
        # Find an element on the page using WebDriverWait with 10-second timeout
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator):
        # Click on an element when it becomes clickable with 10-second timeout
        element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        # Enter text into a field after clearing it with 10-second timeout
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_page_title(self):
        # Return the current page title
        return self.browser.title

    def send_key_from_keyboard(self, key):
        # Send a specific key from the keyboard
        self.browser.send_keys(key)

    def get_field_text(self, locator):
        # Retrieve text from a specified field with 10-second timeout
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
        return element.text

    def find_elements(self, locator):
        # Find multiple elements on the page with 10-second timeout
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(locator)
        )

    def is_element_present(self, locator):
        # Check if an element exists on the page with 10-second timeout
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
        except:
            return False
        return True

    def upload_file(self, locator, file_path):
        # Upload a file to a specified element with 10-second timeout
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
        element.send_keys(file_path)

    def take_full_screenshot(self, name="full_screenshot"):
        # Устанавливаем размер окна равным полной высоте страницы
        total_height = self.browser.execute_script("return document.body.scrollHeight")
        self.browser.set_window_size(1920, total_height)  # Ширина фиксирована, высота — полная
        # Задержка 3 секунды перед скриншотом
        import time
        time.sleep(3)
        screenshot = self.browser.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=AttachmentType.PNG)