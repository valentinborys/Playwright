import pytest
from playwright.sync_api import sync_playwright

# chromium, firefox, webkit - select the desired browser

@pytest.fixture(scope="function")
def browser(request):
    browser_type = request.param if hasattr(request, 'param') else 'chromium'
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=True)
        yield browser
        browser.close()