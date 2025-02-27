import time
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from pages.Registration_page import Registration


# chromium, firefox, webkit - select the desired browser

@pytest.mark.smoke
def test_login(browser):
    fill_form = Registration()
    page = browser.new_page()
    page.goto("https://epicentrk.ua/shop/rozetki/")
    fill_form.fill_registration_form(page)

    expect(page.get_by_text("Добро пожаловать!")).to_have_text("Добро пожаловать!")
