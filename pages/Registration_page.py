import time
from playwright.async_api import Page
from pages.BasePage import BasePage


class Registration(BasePage):

    @staticmethod
    def fill_registration_form(page: Page):
        page.wait_for_timeout(3000)
        page.locator("text=Войти").click()
        page.wait_for_timeout(1000)
        page.locator("text=Регистрация").click()
        page.locator("//input[@name='lastName']").fill('Valentyn')
        page.locator("(//input[@class='_vrmZib'])[9]").fill('Borys')
        page.locator("//input[@name='phone']").fill('380661418400')
        page.locator("(//input[@ type='email'])[2]").fill('test@test.com')
        page.locator("(//input[@type='password'])[1]").type('123QWEasD!@#')
        page.locator("(//input[@type='password'])[2]").type('123QWEasD!@#')
        page.locator("//button[@class='_etcHyp _W7H2r6 _WuoKbT']").click()