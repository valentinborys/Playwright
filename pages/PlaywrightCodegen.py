import random
from pages.BasePage import BasePage


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