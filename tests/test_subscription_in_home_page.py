import pytest

from pages.home_page import HomePage
from pages.verify_subscription_in_home_page import VerifySubscription
from utils.test_data import Data
from utils.tools import take_screenshot


class TestSubscriptionInHomePage:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.subscription = VerifySubscription(self.page)

    def test_subscription_home_page(self, test_setup):
        """
        Test to verify Subscription in home page.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.verify_that_home_page_is_visible()
        self.subscription.scroll_to_the_footer()
        self.subscription.verify_text_subscription()
        self.subscription.input_email_in_field(Data.email)
        self.subscription.click_subscription_button()
        self.subscription.verify_success_message_is_visible()
        take_screenshot(self.page, "subscription_in_home_page")
