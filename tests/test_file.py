import pytest
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_vitamin(browser):
    wait = WebDriverWait(browser, 10)

    vitamin_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/ru/vitamin"]')))
    browser.execute_script("arguments[0].click();", vitamin_button)
    time.sleep(2)

    vitamin_a = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="/ru/vitamin/vitamin_a"]')))
    browser.execute_script("arguments[0].click();", vitamin_a)
    time.sleep(2)

