from tests.pageObjects.basePage import BasePage


class SignInPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator_sign_in_btn = page.locator('[data-action = "sign in]')
        self.locator_email_input = page.locator('#identifierId')
        self.locator_next_btn = page.locator('#identifierNext')
        self.locator_password_input = page.locator('[name="Passwd"]')
        self.locator_password_next_btn = page.locator('#passwordNext')
        self.locator_not_now_btn = page.locator('#passwordNext')
