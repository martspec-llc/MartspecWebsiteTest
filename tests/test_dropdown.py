import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.home_page import HomePage

@pytest.mark.parametrize('dropdown_about', ['/about', '/team', '/careers'])
def test_dropdown_about_us(browser, dropdown_about):

    about_us = (HomePage(browser)
                .click_dropdown_about_us()
                .select_element_dropdown_about_us(dropdown_about)
                )

    assert about_us in browser.current_url


pages = ['/bodymass', '/bodysize', '/calcium', '/electrolyte', 
'/emotion', '/iron', '/magnesium', '/vitamin', '/waistline', '/bodyzinc']

@pytest.mark.parametrize('dropdown_devices', pages)
def test_dropdown_devices(browser, dropdown_devices):

    all_devices = (HomePage(browser)
                .click_dropdown_all_devices()
                .select_element_dropdown_all_devices(dropdown_devices)
                )

    assert all_devices in browser.current_url


@pytest.mark.parametrize('language_text', ['عربي', 'English', 'Русский', 'Deutsch', 'हिन्दी', 'Español',
                                                'Français', '中文', '日本語', 'Português', 'Українська'])
def test_dropdown_language(browser, language_text):

    language = (HomePage(browser)
                .click_dropdown_language()
                .select_element_dropdown_language(language_text)
                )

    assert language.text == language_text
