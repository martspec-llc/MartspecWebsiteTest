import pytest
import requests
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
from utils.sitemap_helper import get_urls_from_sitemap

# Obtém a lista de URLs
target_urls = get_urls_from_sitemap()


def create_resilient_session(retries: int = 3, backoff_factor: float = 1.0) -> requests.Session:
    """
    Creates a resilient HTTP session that automatically retries
    on 503, 429, 502, and 504 errors and network connection failures.
    """
    session = requests.Session()
    retry_strategy = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"],
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


class TestSeoHeadMetadata:

    http_client = create_resilient_session(retries=3, backoff_factor=1.0)

    @pytest.mark.parametrize("url", target_urls)
    def test_seo_head_metadata(self, url):
        """
        Validates SEO, Open Graph, canonical, and hreflang tags
        directly via HTTP request (without browser overhead).
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MartspecSeoBot/1.0; +https://martspec.com)"
        }

        try:
            response = self.http_client.get(url, headers=headers, timeout=12)
        except requests.RequestException as e:
            pytest.fail(f"❌ Connection failed {url}: {str(e)}")

        assert response.status_code == 200, f"❌ Broke link or Redirecting (Status {response.status_code}): {url}"

        soup = BeautifulSoup(response.text, "html.parser")
        errors = []

        # 1. Page Title
        title_tag = soup.find("title")
        title = title_tag.text.strip() if title_tag else None
        if not title or len(title) < 3:
            errors.append("Title missing or less than 3 characters long")

        # 2. Meta Description
        desc_tag = soup.find("meta", attrs={"name": "description"})
        description = desc_tag.get("content", "").strip() if desc_tag else None
        if not description or len(description) < 20:
            errors.append("Meta description missing or less than 20 characters")

        # 3. Open Graph Title
        og_title_tag = soup.find("meta", attrs={"property": "og:title"})
        og_title = og_title_tag.get("content", "").strip() if og_title_tag else None
        if not og_title:
            errors.append("og:Missing title")

        # 4. Open Graph Image
        og_image_tag = soup.find("meta", attrs={"property": "og:image"})
        og_image = og_image_tag.get("content", "").strip() if og_image_tag else None
        if not og_image or not og_image.startswith("http"):
            errors.append("og:Missing image or invalid link")

        # 5. Canonical URL
        canonical_tag = soup.find("link", attrs={"rel": "canonical"})
        canonical = canonical_tag.get("href", "").strip() if canonical_tag else None
        if not canonical or not canonical.startswith("http"):
            errors.append("Canonical tag is missing or not absolute.")

        # 6. Hreflangs (i18n)
        hreflang_tags = soup.find_all("link", attrs={"rel": "alternate", "hreflang": True})
        if len(hreflang_tags) == 0:
            errors.append("Missing hreflang tags for internationalization")

        # Report ALL problems found on this page at once.
        if errors:
            pytest.fail(f"❌ SEO Issues in the URL [{url}]:\n" + "\n".join(f"  - {err}" for err in errors))
