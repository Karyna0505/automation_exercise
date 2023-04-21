import pytest

from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.personal_profile_page import PersonalProfilePage
from utils.test_data import Data
from pages.cart_page import CartPage
from pages.payment_page import PaymentPage
from utils.tools import take_screenshot


@pytest.mark.usefixtures("page", "registered_user", "add_product_to_cart")
class TestPlaceOrderRegisterBeforeCheckout:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.signup_login = SignupLoginPage(self.page)
        self.personal_profile = PersonalProfilePage(self.page)
        self.cart_page = CartPage(self.page)
        self.payment_page = PaymentPage(self.page)

    def test_place_order_register_before_checkout(self, test_setup):
        """
        Test to verify Register before Checkout.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        delivery_address = self.cart_page.get_delivery_address().inner_text().lower()
        assert delivery_address == f"YOUR DELIVERY ADDRESS\nMr. {Data.firstname} {Data.lastname}\n{Data.companyname}\n{Data.address1}\n{Data.address2}\n{Data.city} {Data.state} {Data.zipcode}\nUnited States\n{Data.phonenumber}".lower()

        delivery_address = self.cart_page.get_billing_address_text().inner_text().lower()
        assert delivery_address == f"YOUR BILLING ADDRESS\nMr. {Data.firstname} {Data.lastname}\n{Data.companyname}\n{Data.address1}\n{Data.address2}\n{Data.city} {Data.state} {Data.zipcode}\nUnited States\n{Data.phonenumber}".lower()

        assert len(self.cart_page.query_selector_all_products()) == 2

        self.cart_page.enter_description_in_comment_text_area()
        self.cart_page.click_place_order_button()
        self.payment_page.enter_payment_details(Data.username, Data.card_number, Data.cvc, Data.expiration_month, Data.expiration_year)
        self.payment_page.click_pay_and_confirm_order_button()
        success_message = self.payment_page.verify_success_message()
        assert success_message.inner_text() == 'Congratulations! Your order has been confirmed!'
        self.personal_profile.click_delete_account_link()
        self.personal_profile.verify_successful_deleted_account()
        self.personal_profile.click_continue2_button()

        take_screenshot(self.page, "register_before_checkout")