from playwright.sync_api import Page, expect


class ReviewForm:

    def __init__(self, page: Page):

        self.page = page
        self.__write_review_title = self.page.locator('[href="#reviews"]')
        self.__input_name = self.page.locator('[id="name"]')
        self.__input_email = self.page.locator('[id="email"]')
        self.__input_review = self.page.locator('[id="review"]')
        self.__submit_button = self.page.locator('[id="button-review"]')
        self.__success_message = self.page.locator('[id="review-section"] span')

    def verify_write_review_title(self) -> None:
        self.__write_review_title.is_visible()

    def set_name_email_review(self, name, email, review) -> None:
        self.__input_name.fill(name)
        self.__input_email.fill(email)
        self.__input_review.fill(review)

    def click_submit_button(self) -> None:
        self.__submit_button.click()

    def verify_success_message(self) -> None:
        expect(self.__success_message).to_have_text('Thank you for your review.')




