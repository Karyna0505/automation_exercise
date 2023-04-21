import pytest

from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.personal_profile_page import PersonalProfilePage
from utils.test_data import Data
from pages.cart_page import CartPage
from utils.tools import take_screenshot


@pytest.mark.usefixtures("page", "registered_user")
class TestVerifyAddressDetailsInCheckout:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.signup_login = SignupLoginPage(self.page)
        self.personal_profile = PersonalProfilePage(self.page)
        self.cart_page = CartPage(self.page)

    def test_verify_address_details_in_checkout_page(self, test_setup):
        """
        Test to Verify address details in checkout page.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.cart_page.hover_first_product()
        self.cart_page.click_add_to_cart_button1()
        self.cart_page.click_continue_shopping_button()
        self.cart_page.hover_second_page()
        self.cart_page.click_add_to_cart_button2()
        self.cart_page.click_continue_shopping_button()

        self.cart_page.click_cart_button_on_header()
        self.cart_page.verify_cart_page()
        self.cart_page.click_proceed_to_checkout_button()
        delivery_address = self.cart_page.get_delivery_address().inner_text().lower()

        assert delivery_address == f"YOUR DELIVERY ADDRESS\nMr. {Data.firstname} {Data.lastname}\n{Data.companyname}\n{Data.address1}\n{Data.address2}\n{Data.city} {Data.state} {Data.zipcode}\nUnited States\n{Data.phonenumber}".lower()

        delivery_address = self.cart_page.get_billing_address_text().inner_text().lower()

        assert delivery_address == f"YOUR BILLING ADDRESS\nMr. {Data.firstname} {Data.lastname}\n{Data.companyname}\n{Data.address1}\n{Data.address2}\n{Data.city} {Data.state} {Data.zipcode}\nUnited States\n{Data.phonenumber}".lower()

        self.personal_profile.click_delete_account_link()
        self.personal_profile.verify_successful_deleted_account()
        self.personal_profile.click_continue2_button()
        take_screenshot(self.page, "verify_address_details_in_checkout")
