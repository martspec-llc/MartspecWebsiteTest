from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):

    def click_dropdown_about_us(self):
        about_us = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'navbarDropdownMain')))
        about_us.click()
        return self


    def select_element_dropdown_about_us(self, dropdown_about):
        element_list = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'ul.dropdown-menu a[href*="{dropdown_about}"]')))
        self.browser.execute_script("arguments[0].click();", element_list)

        return dropdown_about


    def click_dropdown_all_devices(self):
        devices = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'navbarDropdownPages')))
        devices.click()
        self.wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul[aria-labelledby="navbarDropdownPages"].show')))
        return self


    def select_element_dropdown_all_devices(self, dropdown_devices):
        element_list = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'ul[aria-labelledby="navbarDropdownPages"] a[href*="{dropdown_devices}"]')))
        self.browser.execute_script("arguments[0].click();", element_list)
        return dropdown_devices

    def click_dropdown_language(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'navbarDropdown')))
        dropdown.click()
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#navbarDropdown + ul.dropdown-menu.show')))
        return self

    def select_element_dropdown_language(self, language_text):
        xpath_locator = f"//a[@id='navbarDropdown']/following-sibling::ul//a[contains(@class, 'dropdown-item') and normalize-space()='{language_text}']"
        click_language = self.wait.until(
            EC.presence_of_element_located((By.XPATH, xpath_locator)))

        self.browser.execute_script("arguments[0].click();", click_language)

        self.wait.until(
            EC.text_to_be_present_in_element((By.ID, 'navbarDropdown'), language_text.strip()))

        return self.browser.find_element(By.ID, 'navbarDropdown')