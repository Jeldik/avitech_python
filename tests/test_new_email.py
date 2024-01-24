from playwright.sync_api import Page, expect

from tests.pageObjects.pageManager import PageManager


def test_attachment(set_up) -> None:
    page = set_up
    pm = PageManager(page)
    pm.inboxPage.locator_new_message.click()
    pm.inboxPage.locator_input_file.set_input_files('./data/zadanie.docx')
    page.reload()

    pm.inboxPage.page.get_by_text("(16 kB)")


def test_open_dialog(set_up) -> None:
    page = set_up
    pm = PageManager(page)
    pm.inboxPage.locator_new_message.click()

    expect(pm.inboxPage.locator_subject).to_be_visible()


def test_pick_contact(set_up) -> None:
    page = set_up
    pm = PageManager(page)
    pm.inboxPage.locator_new_message.click()
    pm.inboxPage.locator_contacts.click()
    pm.inboxPage.locator_contact.click()
