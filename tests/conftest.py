import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="function")
def set_up_tear_down(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(storage_state='../data/storage.json')
    page = context.new_page()
    page.goto("https://mail.google.com/mail/")

    yield page
