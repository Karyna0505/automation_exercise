import pytest
import random
import string
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.signup_form_page import SignupFormPage
from pages.personal_profile_page import PersonalProfilePage
from utils.test_data import Data
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
    page.random_email = generate_random_email()
    signup_login.verify_new_user_title_visible()
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
class TestLoginUserWithValidData:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.signup_login = SignupLoginPage(self.page)
        self.personal_profile = PersonalProfilePage(self.page)

    def test_login_user_with_valid_data(self, test_setup):
        """
        Test to verify user is logging in platform with valid data.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.click_signup_login_button()

        self.signup_login.verify_login_to_your_account_title_visible()
        self.signup_login.enter_login_email(self.page.random_email)
        self.signup_login.enter_login_password(Data.password)
        self.signup_login.click_login_button()

        self.personal_profile.check_logged_in_page()

        self.personal_profile.click_delete_account_link()
        self.personal_profile.verify_successful_deleted_account()
        self.personal_profile.click_continue2_button()

        take_screenshot(self.page, "loging_user_with_valid_data")
