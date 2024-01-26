import time
from tests.pageObjects.pageManager import PageManager


def test_login(playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    pm = PageManager(page)

    page.goto("https://mail.google.com/mail/")

    pm.signInPage.locator_email_input.fill('jeldicek@gmail.com')
    pm.signInPage.locator_next_btn.click()
    pm.signInPage.locator_password_input.fill('Jelinek81')
    pm.signInPage.locator_password_next_btn.click()

    time.sleep(5)
    context.storage_state(path="../data/storage.json")
