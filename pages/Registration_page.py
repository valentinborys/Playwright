import time
from playwright.async_api import Page
from pages.BasePage import BasePage
from locators import RegistrationLocators


class Registration(BasePage):

    @staticmethod
    def open_main_page(page):
        page.goto("https://epicentrk.ua/shop/rozetki/")

    @staticmethod
    def fill_registration_form(page: Page):
        page.wait_for_timeout(2000)
        page.locator(RegistrationLocators.ENTRANCE_LOCATOR).click()
        page.wait_for_timeout(1000)
        page.locator(RegistrationLocators.REGISTRATION_LOCATOR).click()
        page.locator(RegistrationLocators.LAST_NAME_LOCATOR).fill('Valentyn')
        page.locator(RegistrationLocators.FIRST_NAME_LOCATOR).fill('Borys')
        page.locator(RegistrationLocators.PHONE).fill('380661418400')
        page.locator(RegistrationLocators.EMAIL).fill('test@test.com')
        page.locator(RegistrationLocators.PASSWORD).type('123QWEasD!@#')
        page.locator(RegistrationLocators.PASSWORD_CONFIRM).type('123QWEasD!@#')
        page.locator(RegistrationLocators.SUCCESS_BUTTON).click()