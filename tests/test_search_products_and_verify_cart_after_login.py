import pytest
import random
import string
from pages.home_page import HomePage
from pages.search_product_page import SearchProduct
from pages.products_page import AllProductsPage
from utils.test_data import Data
from pages.cart_page import CartPage
from pages.signup_login_page import SignupLoginPage
from pages.signup_form_page import SignupFormPage
from pages.personal_profile_page import PersonalProfilePage
from utils.tools import take_screenshot


def generate_random_email():
    letters = string.ascii_lowercase
    email = ''.join(random.choice(letters) for i in range(10))
    email += '@example.com'
    return email


@pytest.fixture
def registered_user(new_page):
    page = new_page
    home_page = HomePage(page)
    signup_login = SignupLoginPage(page)
    signup_form = SignupFormPage(page)
    personal_profile = PersonalProfilePage(page)

    home_page.verify_that_home_page_is_visible()
    home_page.click_signup_login_button()

    signup_login.verify_new_user_title_visible()
    page.random_email = generate_random_email()
    signup_login.enter_name(Data.username)
    signup_login.enter_email(page.random_email)
    signup_login.click_signup_button()

    signup_form.check_enter_account_information_title()
    signup_form.click_title_radio_button()
    signup_form.set_password(Data.password)
    signup_form.select_date_of_birth()
    signup_form.check_checkboxes()

    signup_form.fill_address_information(Data.firstname, Data.lastname, Data.companyname, Data.address1, Data.address2, Data.state, Data.city, Data.zipcode, Data.phonenumber)
    signup_form.click_create_account()

    signup_form.check_account_created_message()
    signup_form.click_continue_button()

    personal_profile.click_logout_button()


@pytest.mark.usefixtures("page", "registered_user")
class TestSearchProductsAndVerifyCartAfterLogin:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.search_product = SearchProduct(self.page)
        self.products_page = AllProductsPage(self.page)
        self.cart_page = CartPage(self.page)
        self.signup_login = SignupLoginPage(self.page)

    def test_search_products_and_verify_cart_after_login(self, test_setup):
        """
        Test to verify Search Products and Verify Cart After Login.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.products_page.click_products_button()

        self.products_page.check_all_products_page_is_visible()
        assert self.page.url == 'https://automationexercise.com/products'

        self.search_product.set_data_in_search_field(Data.searchdata)
        self.search_product.click_search_button()
        self.search_product.verify_searched_product_title_is_visible()
        self.search_product.verify_all_products_related_to_search_are_visible()
        self.search_product.hover_first_product()
        self.search_product.click_add_to_cart_button1()
        self.cart_page.click_continue_shopping_button()
        self.search_product.hover_second_product()
        self.search_product.click_add_to_cart_button2()
        self.cart_page.click_view_cart()
        assert len(self.page.query_selector_all('tbody>tr')) == 2
        self.home_page.click_signup_login_button()

        self.signup_login.verify_login_to_your_account_title_visible()
        self.signup_login.enter_login_email(self.page.random_email)
        self.signup_login.enter_login_password(Data.password)
        self.signup_login.click_login_button()
        self.home_page.click_cart_button()
        self.search_product.verify_first_product_is_visible()
        self.search_product.verify_second_product_is_visible()
        take_screenshot(self.page, "search_products_and_verify_cart_after_login")
