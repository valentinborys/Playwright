import pytest
from playwright.sync_api import sync_playwright

# chromium, firefox, webkit - select the desired browser

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()