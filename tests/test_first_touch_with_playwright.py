from playwright.sync_api import Page, expect

# pytest --headed

def test_one(page: Page):
    page.goto('https://www.pravda.com.ua/news/2025/02/26/7500246/')
    expect(page.get_by_text('У Румунії заарештували проросійського екскандидата у президенти').nth(0)).to_be_visible()


def test_second(page: Page):
    page.goto('https://www.pravda.com.ua/news/2025/02/26/7500292/')

    page.locator('div.post_text > p:nth-child(2) > a').click()
    expect(page.locator("#endless7205944")).to_have_text("повідомило")
