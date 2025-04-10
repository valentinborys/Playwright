import time

from pages.PlaywrightCodegen import *
import pytest
from playwright.sync_api import expect

class TestCodegen(BasePage):

    @pytest.mark.parametrize("browser", ["firefox"], indirect=True)
    @pytest.mark.skip
    def test_playwright_codegen(self, browser) -> None:

        # Create a new browser context
        context = browser.new_context()
        page = context.new_page()

        # Create an instance of the form handler class
        pl_codegen = PlaywrightPage()

        # Open the target page
        page.goto("https://ithillel.ua/")

        # Fill out and submit the form
        pl_codegen.fill_test_form(page)

        time.sleep(10)
        # Verify that the success message is displayed
        expect(page.get_by_text("Відправлено")).to_be_visible(timeout=5000)


    def test_project_manegmant_registration(self, browser):

        # Create a new browser context
        context = browser.new_context()
        page = context.new_page()
        pl_codegen = PlaywrightPage()

        # Open the target page
        page.goto("https://ithillel.ua/")

        # Fill out and submit the form
        pl_codegen.fill_project_manegmant_registration(page)

        # Verify that the success message is displayed
        expect(page.get_by_text("Ви ввели невірну адресу електронної пошти або пароль")).to_have_text('Ви ввели невірну адресу електронної пошти або пароль')


