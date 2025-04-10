import playwright


def test_hille(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ithillel.ua/")
    page.get_by_role("button", name="Безкоштовна консультація").click()
    page.get_by_role("textbox", name="Iм'я").click()
    page.get_by_role("textbox", name="Iм'я").fill("Валентин")
    page.get_by_role("textbox", name="Iм'я").press("Tab")
    page.get_by_role("textbox", name="Email", exact=True).fill("test@test.com")
    page.get_by_role("textbox", name="Телефон").click()
    page.get_by_role("textbox", name="Телефон").fill("66 666 66666")
    page.get_by_role("button", name="Оберіть").click()
    page.get_by_text("ПрограмуванняFull-Stack —").click()
    page.locator("#field-comment-consultation div").filter(has_text="Коментар").click()
    page.get_by_placeholder("Ви можете уточнити ваше питання, це допоможе нам краще провести консультацію для").click()
    page.get_by_placeholder("Ви можете уточнити ваше питання, це допоможе нам краще провести консультацію для").fill("test")
    with page.expect_popup() as page1_info:
        page.locator("#form-consultation label").filter(has_text="Згоден на обробку персональних даних").click()
    page1 = page1_info.value
    page1.close()
    page.locator("#form-consultation label").filter(has_text="Згоден на обробку персональних даних").locator("span").click()
    page.get_by_role("button", name="Залишити запит").click()