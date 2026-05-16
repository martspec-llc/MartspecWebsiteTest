from pages.base_page import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def click_dropdown_about_us(self):
        about_us = self.browser.find_element(By.ID, 'navbarDropdownMain')
        about_us.click()
        return self


    def click_element_dropdown_about_us(self, dropdown_about):
        element_list = self.browser.find_element(
            By.CSS_SELECTOR, f'ul.dropdown-menu a[href*="{dropdown_about}"]')
        element_list.click()
        return dropdown_about
