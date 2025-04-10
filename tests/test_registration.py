import pytest
from playwright.sync_api import expect
from pages.BasePage import BasePage
from pages.Registration_page import Registration

class TestCodegen(BasePage):
    @pytest.mark.smoke
    @pytest.mark.skip
    @pytest.mark.parametrize("browser", ["chromium"], indirect=True)
    def test_login_chromium(self, browser):
        registration = Registration()
        page = browser.new_page()

        registration.open_main_page(page)
        registration.fill_registration_form(page)

        expect(page.get_by_text("Добро пожаловать!")).to_have_text("Добро пожаловать!")


    @pytest.mark.smoke
    @pytest.mark.parametrize("browser", ["firefox"], indirect=True)
    def test_login_firefox(self, browser):
        registration = Registration()
        page = browser.new_page()

        registration.open_main_page(page)
        registration.fill_registration_form(page)

        expect(page.get_by_text("Добро пожаловать!")).to_have_text("Добро пожаловать!")
