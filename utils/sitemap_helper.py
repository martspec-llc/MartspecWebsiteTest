import xml.etree.ElementTree as ET
import requests

def get_urls_from_sitemap(sitemap_url="https://martspec.com/sitemap.xml", limit=None):
    """
    Fetches and parses the sitemap.xml to extract all page URLs.
    :param sitemap_url: The direct target URL of the sitemap XML.
    :param limit: Optional integer to limit the number of returned URLs (useful for quick local runs).
    :return: List of URL strings found in the sitemap.
    """
    try:
        # Fetch the sitemap XML content
        response = requests.get(sitemap_url, timeout = 10)
        response.raise_for_status()

        # Parse XML structure
        root = ET.fromstring(response.content)

        # Extract elements ending with 'loc' (handles any XML namespace seamlessly)
        urls = [elem.text for elem in root.iter() if elem.tag.endswith('loc') and elem.text]

        # Apply optional execution limit
        if limit and isinstance(limit, int):
            return urls [:limit]

        return urls

    except Exception as e:
        print(f"⚠️ Failed to fetch or parse sitemap: {e}")
        # Fallback list of key URLs in case of network parsing issues
        return [
            "https://martspec.com/",
            "https://martspec.com/vitamin",
            "https://martspec.com/bodysize"
        ]