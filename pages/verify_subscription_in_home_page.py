from playwright.sync_api import Page


class VerifySubscription:

    def __init__(self, page: Page):

        self.page = page

        self.__subscription_field = self.page.locator('[id="susbscribe_email"]')
        self.__subscription_title = self.page.locator('footer h2')
        self.__subscription_button = self.page.locator('[id="subscribe"]')
        self.__successful_message = self.page.locator('[id="success-subscribe"] div')

    def scroll_to_the_footer(self) -> None:
        self.page.locator('[id="footer"]').scroll_into_view_if_needed()

    def verify_text_subscription(self) -> None:
        self.__subscription_title.is_visible()

    def input_email_in_field(self, email) -> None:
        self.__subscription_field.fill(email)

    def click_subscription_button(self) -> None:
        self.__subscription_button.click()

    def verify_success_message_is_visible(self) -> None:
        self.__successful_message.is_visible()


