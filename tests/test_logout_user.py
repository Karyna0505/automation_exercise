import pytest


from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.personal_profile_page import PersonalProfilePage
from utils.test_data import Data
from utils.tools import take_screenshot


@pytest.mark.usefixtures("page", "registered_user_logout")
class TestLogoutUser:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.signup_login = SignupLoginPage(self.page)
        self.personal_profile = PersonalProfilePage(self.page)

    def test_logout_user(self, test_setup):
        """
        Test to verify user is logging out.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.click_signup_login_button()

        self.signup_login.verify_login_to_your_account_title_visible()
        self.signup_login.enter_login_email(self.page.random_email)
        self.signup_login.enter_login_password(Data.password)
        self.signup_login.click_login_button()

        self.personal_profile.check_logged_in_page()
        self.personal_profile.click_logout_button()
        assert self.page.url == f"{Data.URL}/login"
        self.signup_login.verify_login_to_your_account_title_visible()

        take_screenshot(self.page, "logout_user")
