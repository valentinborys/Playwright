from pages.PlaywrightCodegen import *
import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("browser", ["firefox"], indirect=True)
def test_playwright_codegen(browser) -> None:

    # Create a new browser context
    context = browser.new_context()
    page = context.new_page()

    # Create an instance of the form handler class
    pl_codegen = PlaywrightPage()

    # Open the target page
    page.goto("https://ithillel.ua/")

    # Fill out and submit the form
    pl_codegen.fill_test_form(page)

    # Verify that the success message is displayed
    expect(page.get_by_text("Відправлено")).to_be_visible(timeout=5000)

