from playwright.sync_api import Page, expect


class ContactUs:

    def __init__(self, page: Page):

        self.page = page

        self.__contact_us_button = self.page.locator('[href="/contact_us"]')
        self.__get_in_touch_title = self.page.get_by_text("Get In Touch")
        self.__name_field = self.page.locator('[data-qa="name"]')
        self.__email_field = self.page.locator('[data-qa="email"]')
        self.__subject_field = self.page.locator('[data-qa="subject"]')
        self.__message_field = self.page.locator('[id="message"]')
        self.__upload_button = self.page.locator('input[type="file"]')
        self.__submit_button = self.page.locator('[data-qa="submit-button"]')
        self.__success_message = self.page.locator('[class="status alert alert-success"]')
        self.__home_button = self.page.get_by_role("link", name=" Home")

    def click_contact_us_button(self) -> None:
        self.__contact_us_button.click()

    def check_get_in_touch_title_is_visible(self) -> None:
        self.__get_in_touch_title.is_visible()

    def set_name(self, name) -> None:
        self.__name_field.fill(name)

    def set_email(self, email) -> None:
        self.__email_field.fill(email)

    def set_subject(self, subject) -> None:
        self.__subject_field.fill(subject)

    def set_message(self, text) -> None:
        self.__message_field.fill(text)

    def upload_file(self) -> None:
        with self.page.expect_file_chooser() as fc_info:
            self.__upload_button.click()
        file_chooser = fc_info.value
        file_chooser.set_files("./utils/test file.docx")

    def click_submit_button(self) -> None:
        self.__submit_button.click()

    def verify_success_message(self) -> None:
        self.__success_message.is_visible()

    def click_home_button(self) -> None:
        self.__home_button.click()

