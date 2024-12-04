from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    main_url = "https://opensource-demo.orangehrmlive.com/web/index.php/"
    def find_element(self, locator, timeout=10):
        """Find an element on the page"""
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator, timeout=10):
        """Click on an element"""
        element = self.find_element(locator, timeout)
        element.click()

    def enter_text(self, locator, text, timeout=10):
        """Enter text into a field"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_page_title(self):
        """Get the page title"""
        return self.browser.title

    def send_key_from_keyboard(self, key):
        """Send a key from the keyboard"""
        self.browser.send_keys(key)
