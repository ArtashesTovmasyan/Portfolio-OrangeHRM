from selenium.webdriver.common.by import By
from pages.base_page import BasePage
ADMIN_ITEM_LOCATOR = (By.XPATH, "//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Admin']")
PIM_ITEM_LOCATOR = (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
LEAVE_ITEM_LOCATOR = (By.XPATH, "//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Leave']")
TIME_ITEM_LOCATOR = (By.XPATH, "//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Time']")
RECRUITMENT_ITEM_LOCATOR = (By.XPATH, "//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Recruitment']")
PERFORMANCE_ITEM_LOCATOR = (By.XPATH, "//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Performance']")
DASHBOARD_ITEM_LOCATOR = (By.XPATH, "//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Dashboard']")
DIRECTORY_ITEM_LOCATOR = (By.XPATH, "//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Directory']")
MAINTENANCE_ITEM_LOCATOR = (By.XPATH, "//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Maintenance']")
BUZZ_ITEM_LOCATOR = (By.XPATH, "//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Buzz']")



class SideBar(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def click_on_admin(self):
        self.click_element(ADMIN_ITEM_LOCATOR)

    def click_on_pim(self):
        self.click_element(PIM_ITEM_LOCATOR)


