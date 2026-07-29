from selenium.webdriver.common.by import By

class SeoPage:
    def __init__(self, driver):
        # Initialize WebDriver instance
        self.driver = driver

    # Retrieve current page title tag
    def get_page_title(self):
        return self.driver.title

    # Retrieve meta tag content attribute by name
    def get_meta_content_by_name(self, name_attr):
        try:
            element = self.driver.find_element(By.XPATH, f'//meta[@name="{name_attr}"]')
            return element.get_attribute("content")
        except:
            return None

    # Retrieve Open Graph meta tag content attribute by property
    def get_meta_content_by_property(self, property_attr):
        try:
            element = self.driver.find_element(By.XPATH, f'//meta[@property="{property_attr}"]')
            return element.get_attribute("content")
        except:
            return None

    # Retrieve canonical link href attribute
    def get_canonical_url(self):
        try:
            element = self.driver.find_element(By.XPATH, '//link[@rel="canonical"]')
            return element.get_attribute("href")
        except:
            return None

    # Retrieve list of all available hreflang language attributes
    def get_hreflang_links(self):
        try:
            elements = self.driver.find_elements(By.XPATH, '//link[@rel="alternate" and @hreflang]')
            return [elem.get_attribute("hreflang") for elem in elements]
        except:
            return []