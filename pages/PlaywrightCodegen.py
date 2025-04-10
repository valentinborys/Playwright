import random
from playwright.async_api import Page
from pages.BasePage import BasePage
import pytest


class PlaywrightPage(BasePage):

    @staticmethod
    def generate_random_phone():
        return f"66 {random.randint(100, 999)} {random.randint(10000, 99999)}"

    @staticmethod
    def fill_test_form(page):
        codegen = PlaywrightPage()
        page.goto("https://ithillel.ua/")
        page.get_by_role("button", name="Безкоштовна консультація").click()
        page.get_by_role("textbox", name="Iм'я").click()
        page.get_by_role("textbox", name="Iм'я").fill("Test")
        page.get_by_role("textbox", name="Email", exact=True).click()
        page.get_by_role("textbox", name="Email", exact=True).fill("test@test.playwright.com")
        page.get_by_role("textbox", name="Телефон").click()
        page.get_by_role("textbox", name="Телефон").fill(codegen.generate_random_phone())
        page.get_by_role("button", name="Оберіть").click()
        page.get_by_placeholder("Пошук", exact=True).click()
        page.get_by_placeholder("Пошук", exact=True).fill("Aut")
        page.get_by_role("option", name="QA Automation – Python").locator("span").click()
        page.get_by_placeholder(
            "Ви можете уточнити ваше питання, це допоможе нам краще провести консультацію для").click()
        page.get_by_placeholder(
            "Ви можете уточнити ваше питання, це допоможе нам краще провести консультацію для").fill("Test test test")
        page.locator("#form-consultation label").filter(has_text="Згоден на обробку персональних даних").locator(
            "span").click()

        page.get_by_role("button", name="Залишити запит").click()

    @staticmethod
    def fill_project_manegmant_registration(page: Page):
        page.get_by_role("link", name="Project Management Start").click()
        page.get_by_role("link", name="Почати зараз").first.click()
        page.wait_for_selector("role=heading[name='Реєстрація']", timeout=60000)
        page.get_by_role("heading", name="Реєстрація").click()
        page.get_by_role("link", name="Увійти до LMS").click()
        page.get_by_placeholder("Пошта").click()
        page.get_by_placeholder("Пошта").fill("vvv@etwtwet.com")
        page.get_by_placeholder("Пароль").click()
        page.get_by_placeholder("Пароль").fill("123123123123142")
        page.get_by_role("button", name="Увійти").click()
