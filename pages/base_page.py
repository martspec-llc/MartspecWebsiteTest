from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)


    def click_logo(self):

        logo = self.browser.find_element(By.CLASS_NAME, 'ms-navbar-brand')
        logo.click()
        return self
