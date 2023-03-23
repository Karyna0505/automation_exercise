import pytest

from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from utils.test_data import Data
from utils.tools import take_screenshot


class TestRegisterUserWithExistingEmail:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.signup_login = SignupLoginPage(self.page)

    def test_register_new_user(self, test_setup):
        """
        Test to verify registration through the Home page with existing email.
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.home_page.verify_that_home_page_is_visible()
        self.home_page.click_signup_login_button()

        self.signup_login.verify_new_user_title_visible()
        self.signup_login.enter_name(Data.username)
        self.signup_login.enter_email(Data.existing_email)
        self.signup_login.click_signup_button()
        self.signup_login.verify_error_message_email_already_exist()
        take_screenshot(self.page, "register_user_with_existing_email")
