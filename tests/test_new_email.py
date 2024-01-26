from playwright.sync_api import expect
from tests.pageObjects.pageManager import PageManager


def test_open_dialog(set_up_tear_down) -> None:
    pm = PageManager(set_up_tear_down)
    pm.inboxPage.locator_new_message.click()

    expect(pm.inboxPage.locator_subject).to_be_visible()


def test_pick_contact(set_up_tear_down) -> None:
    pm = PageManager(set_up_tear_down)
    pm.inboxPage.locator_new_message.click()
    pm.inboxPage.locator_contacts.click()
    pm.inboxPage.locator_contact.click()
    pm.inboxPage.locator_insert.click()

    expect(pm.inboxPage.locator_selected_contact).to_be_visible()


def test_logout(set_up_tear_down) -> None:
    pm = PageManager(set_up_tear_down)
    pm.inboxPage.locator_profile.click()
    pm.inboxPage.locator_logout.click()

    expect(pm.inboxPage.page.locator('body')).to_contain_text('Sign in')


def test_add_attachment(set_up_tear_down) -> None:
    pm = PageManager(set_up_tear_down)
    pm.inboxPage.locator_new_message.click()
    pm.inboxPage.locator_input_file.set_input_files('../data/zadanie.docx')
    set_up_tear_down.reload()

    pm.inboxPage.page.get_by_text("(16 kB)")
