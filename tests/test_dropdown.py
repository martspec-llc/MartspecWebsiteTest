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


pages = ['/bodymass', '/vitamin', '/iron', '/calcium', '/magnesium',
'/waistline', '/bodysize', '/bodyzinc', '/electrolyte', '/emotion']

@pytest.mark.parametrize('dropdown_devices', pages)
def test_dropdown_devices(browser, dropdown_devices):

    all_devices = (HomePage(browser)
                   .click_dropdown_all_devices()
                   .select_element_dropdown_all_devices(dropdown_devices)
                   )

    assert all_devices in browser.current_url


@pytest.mark.parametrize('dropdown_language', ['/ar', '/de', '/hi', '/es', '/fr',
                                                '/zh', '/ja', '/pt', '/uk'])
def test_dropdown_language(browser, dropdown_language):

    language = (HomePage(browser)
                .click_dropdown_language()
                .select_element_dropdown_language(dropdown_language)
                )

    assert language in browser.current_url
