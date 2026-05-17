from pages.base_page import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def click_dropdown_about_us(self):
        about_us = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'navbarDropdownMain')))
        about_us.click()
        return self


    def select_element_dropdown_about_us(self, dropdown_about):
        element_list = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'ul.dropdown-menu a[href*="{dropdown_about}"]')))
        element_list.click()
        return dropdown_about


    def click_dropdown_all_devices(self):
        devices = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'navbarDropdownPages')))
        devices.click()
        return self


    def select_element_dropdown_all_devices(self, dropdown_devices):
        element_list = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'ul.dropdown-menu a[href*="{dropdown_devices}"]')))
        element_list.click()
        return dropdown_devices


    def click_dropdown_language(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'navbarDropdown')))
        dropdown.click()
        return self


    def select_element_dropdown_language(self, language_text):
        click_language = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, language_text)))
        click_language.click()

        self.wait.until(
            EC.text_to_be_present_in_element((By.ID, 'navbarDropdown'), language_text))
        return self.browser.find_element(By.ID, 'navbarDropdown')
