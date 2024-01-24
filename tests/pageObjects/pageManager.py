from tests.pageObjects.aboutPage import AboutPage
from tests.pageObjects.basePage import BasePage
from tests.pageObjects.inboxPage import InboxPage
from tests.pageObjects.signInPage import SignInPage


class PageManager(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.aboutPage = AboutPage(page)
        self.signInPage = SignInPage(page)
        self.inboxPage = InboxPage(page)
