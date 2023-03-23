from playwright.sync_api import Page


class PaymentPage:

    def __init__(self, page: Page):

        self.page = page
        self.__name_on_card_field = self.page.locator('[name="name_on_card"]')
        self.__card_number_field = self.page.locator('[name="card_number"]')
        self.__cvc_field = self.page.locator('[name="cvc"]')
        self.__expiration_month = self.page.locator('[name="expiry_month"]')
        self.__expiration_year = self.page.locator('[name="expiry_year"]')
        self.__pay_and_confirm_order_button = self.page.locator('[id="submit"]')
        self.__success_message = self.page.locator('section p')
        self.__download_invoice = self.page.locator('[href="/download_invoice/900"]')
        self.__continue_button = self.page.locator('[data-qa="continue-button"]')

    def enter_payment_details(self, name, number, cvc, month, year) -> None:
        self.__name_on_card_field.fill(name)
        self.__card_number_field.fill(number)
        self.__cvc_field.fill(cvc)
        self.__expiration_month.fill(month)
        self.__expiration_year.fill(year)

    def click_pay_and_confirm_order_button(self) -> None:
        self.__pay_and_confirm_order_button.click()

    def verify_success_message(self) -> None:
        assert self.__success_message.inner_text() == 'Congratulations! Your order has been confirmed!'

    def click_download_invoice_button(self) -> None:
        self.__download_invoice.click()

    def click_continue_button(self) -> None:
        self.__continue_button.click()




