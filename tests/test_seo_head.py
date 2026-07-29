import pytest
from pages.seo_page import SeoPage

# List of target URLs for parameterized SEO validation
TARGET_URLS = [
    "https://martspec.com/",
    "https://martspec.com/vitamin",
    "https://martspec.com/bodysize"
]

class TestSeoHeadMetadata:

    @pytest.mark.parametrize("url", TARGET_URLS)
    def test_seo_head_metadata(self, browser, url):
        """
        Validates visual <head> metadata tags for technical SEO,
        Open Graph social preview, canonical indexing, and i18n compliance.
        """
        browser.get(url)
        seo_page = SeoPage(browser)

        # Extract DOM metadata from <head>
        title = seo_page.get_page_title()
        description = seo_page.get_meta_content_by_name("description")
        og_title = seo_page.get_meta_content_by_property("og:title")
        og_image = seo_page.get_meta_content_by_property("og:image")
        canonical = seo_page.get_canonical_url()
        hreflangs = seo_page.get_hreflang_links()

        # Check 1: Title tag must exist and meet minimum length
        assert title is not None and len(title) > 5, f"❌ Invalid or missing title in the URL: {url}"

        # Check 2: Meta description must exist and meet minimum length
        assert description is not None and len(description) >=20, f"❌ Missing or too short (<20 chars) description for the URL: {url}"

        # Check 3: Open Graph title must exist
        assert og_title is not None and len(og_title) > 0, f"❌ og:title missing from URL: {url}"

        # Check 4: Open Graph image must exist and be a valid URL
        assert og_image is not None and og_image.startswith("http"), f"❌ og:Missing image or invalid link in the URL: {url}"

        # Check 5: Canonical link must exist and be a valid URL
        assert canonical is not None and canonical.startswith("http"), f"❌ Missing canonical link on URL: {url}"

        # Check 6: Hreflang alternate tags must be present for i18n
        assert len(hreflangs) > 0, f"❌ No hreflang i18n tags found on URL: {url}"



        # Print Log after Tests
        print(f"\n--- [LOG SEO] URL: {url} ---")
        print(f"📌 TITLE: {title}")
        print(f"📌 DESCRIPTION: {description}")
        print(f"📌 OG:TITLE: {og_title}")
        print(f"📌 OG:IMAGE: {og_image}")
        print(f"\n🔗 CANONICAL URL: {canonical}")
        print(f"🌍 HREFLANG LIST ({len(hreflangs)} languages): {hreflangs}")