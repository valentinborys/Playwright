import time
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


class BasePage:

    @staticmethod
    def wait_for_element_with_reload(page: Page, locator: str, timeout: int = 5000, max_retries: int = 3):

        for attempt in range(max_retries):
            try:
                page.locator(locator).wait_for(state="visible", timeout=timeout)
                return True
            except PlaywrightTimeoutError:
                if attempt < max_retries - 1:
                    page.reload()
                    time.sleep(2)
                else:
                    return False

        return False
