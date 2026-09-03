from bs4 import BeautifulSoup

class SeoPage:
    def __init__(self, html_content:str):
        self.soup = BeautifulSoup(html_content, "html.parser")

    # Retrieve current page title tag
    def get_page_title(self):
        tag = self.soup.find("title")
        return tag.text.strip() if tag else None

    # Retrieve meta tag content attribute by name
    def get_meta_content_by_name(self, name_attr):
        tag = self.soup.find("meta", attrs={"name": name_attr})
        return tag.get("content", "").strip() if tag and tag.get("content") else None

    # Retrieve Open Graph meta tag content attribute by property
    def get_meta_content_by_property(self, property_attr):
        tag = self.soup.find("meta", attrs={"property": property_attr})
        return tag.get("content", "").strip() if tag and tag.get("content") else None

    # Retrieve canonical link href attribute
    def get_canonical_url(self):
        tag = self.soup.find("link", attrs={"rel": "canonical"})
        return tag.get("href", "").strip() if tag and tag.get("href") else None

    # Retrieve list of all available hreflang language attributes
    def get_hreflang_links(self):
        tags = self.soup.find_all("link", attrs={"rel": "alternate", "hreflang": True})
        return [tag.get("hreflang") for tag in tags if tag.get("hreflang")]