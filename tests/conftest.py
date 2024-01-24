import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

from tests.pageObjects.pageManager import PageManager


@pytest.fixture(scope="function")
def set_up(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    pm = PageManager(page)

    page.goto("https://mail.google.com/mail/")

    pm.signInPage.locator_email_input.fill('jeldicek@gmail.com')
    pm.signInPage.locator_next_btn.click()
    pm.signInPage.locator_password_input.fill('Jelinek81')
    pm.signInPage.locator_password_next_btn.click()

    yield page

    context.close()
    browser.close()
