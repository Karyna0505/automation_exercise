import pytest

from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from utils.test_data import Data
from utils.tools import take_screenshot


class TestLoginUserWithInvalidData:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.signup_login = SignupLoginPage(self.page)

    def test_login_user_with_invalid_data(self, test_setup):
        """
        Test to verify user is logging in platform with invalid data.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.verify_that_home_page_is_visible()
        self.home_page.click_signup_login_button()

        self.signup_login.verify_login_to_your_account_title_visible()
        self.signup_login.enter_login_email(Data.invalid_email)
        self.signup_login.enter_login_password(Data.invalid_password)
        self.signup_login.click_login_button()
        self.signup_login.verify_error_message_is_visible()

        take_screenshot(self.page, "loging_user_with_invalid_data")
