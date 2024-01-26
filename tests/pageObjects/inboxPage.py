from tests.pageObjects.basePage import BasePage


class InboxPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator_new_message = page.locator(':nth-match(:text("Nová zpráva"), 1)')
        self.locator_contacts = page.locator(':nth-match([data-tooltip="Vybrat kontakty"], 1)')
        self.locator_recipients = page.get_by_text('Příjemci')
        self.locator_send = page.locator('[data-tooltip="Odeslat ‪(Ctrl +Enter)‬"]')
        self.locator_frame = page.frame_locator('iframe[src*="docs.google"]')
        self.locator_contact = self.locator_frame.locator('div[id~="jeldicek@gmail.com"]:nth-child(1)')
        self.locator_insert = self.locator_frame.get_by_text('Vložit')
        self.locator_input_file = page.locator('input[type=file]')
        self.locator_profile = page.get_by_label("Účet Google: Tomáš Jelínek  \n(jeldicek@gmail.com)")
        self.locator_account_frame = page.frame_locator('iframe[name="account"]')
        self.locator_logout = self.locator_account_frame.get_by_text('Odhlásit se')
        self.locator_subject = page.get_by_placeholder('Předmět')
        self.locator_selected_contact = page.get_by_text('(gmail.com)')
