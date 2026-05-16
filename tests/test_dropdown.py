import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.home_page import HomePage

@pytest.mark.parametrize('dropdown_about', ['/about', '/team', '/careers'])
def test_dropdown_about_us(browser, dropdown_about):

    about_us = (HomePage(browser)
                .click_dropdown_about_us()
                .click_element_dropdown_about_us(dropdown_about)
                )

    assert about_us in browser.current_url


pages = ['/bodymass', '/vitamin', '/iron', '/calcium', '/magnesium',
'/waistline', '/bodysize', '/bodyzinc', '/electrolyte', '/emotion']

@pytest.mark.parametrize('dropdown_devices', pages)
def test_dropdown_devices(browser, dropdown_devices):
    wait = WebDriverWait(browser, 5)

    devices = browser.find_element(By.ID, 'navbarDropdownPages')
    devices.click()

    click_element = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f'ul.dropdown-menu a[href*="{dropdown_devices}"]')))
    click_element.click()

    assert dropdown_devices in browser.current_url


languages = ['/ar', '/en', '/de', '/hi', '/es', '/fr', '/zh', '/ja', '/pt', '/uk']

@pytest.mark.parametrize('dropdown_language', languages)
def test_dropdown_language(browser, dropdown_language):
    wait = WebDriverWait(browser, 5)

    dropdown = browser.find_element(By.ID, 'navbarDropdown')
    dropdown.click()

    click_language = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f'ul.dropdown-menu a[href*="{dropdown_language}"]')))
    click_language.click()

    assert dropdown_language in browser.current_url
