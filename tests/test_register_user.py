import pytest

from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.signup_form_page import SignupFormPage
from pages.personal_profile_page import PersonalProfilePage
from utils.test_data import Data
from utils.tools import take_screenshot, generate_random_email


class TestRegisterUser:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.signup_login = SignupLoginPage(self.page)
        self.signup_form = SignupFormPage(self.page)
        self.personal_profile = PersonalProfilePage(self.page)

    def test_register_new_user(self, test_setup):
        """
        Test to verify registration through the Home page.
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.home_page.verify_that_home_page_is_visible()
        self.home_page.click_signup_login_button()
        self.page.random_email = generate_random_email()
        self.signup_login.verify_new_user_title_visible()
        self.signup_login.enter_name(Data.username)
        self.signup_login.enter_email(self.page.random_email)
        self.signup_login.click_signup_button()

        self.signup_form.check_enter_account_information_title()
        self.signup_form.click_title_radio_button()
        self.signup_form.set_password(Data.password)
        self.signup_form.select_date_of_birth()
        self.signup_form.check_checkboxes()

        self.signup_form.fill_address_information(Data.firstname, Data.lastname, Data.companyname, Data.address1, Data.address2, Data.state, Data.city, Data.zipcode, Data.phonenumber)
        self.signup_form.click_create_account()

        self.signup_form.check_account_created_message()
        self.signup_form.click_continue_button()

        self.personal_profile.check_logged_in_page()

        self.personal_profile.click_delete_account_link()
        self.personal_profile.verify_successful_deleted_account()
        self.personal_profile.click_continue2_button()
        take_screenshot(self.page, "register_user")