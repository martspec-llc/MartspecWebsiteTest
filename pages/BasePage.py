def test_logo(browser):

    logo = browser.find_element(By.CLASS_NAME, 'ms-navbar-brand')
    logo.click()