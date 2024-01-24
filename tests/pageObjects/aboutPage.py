from tests.pageObjects.basePage import BasePage


class AboutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator_sign_in_btn = page.locator('[data-action = "sign in]')
