import pytest

from pages.home_page import HomePage
from pages.verify_subscription_in_home_page import VerifySubscription
from utils.tools import take_screenshot


class TestScrollUpInHomePage:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.subscription = VerifySubscription(self.page)

    def test_scroll_up_on_home_page(self, test_setup):
        """
        Test to Verify Scroll Up without 'Arrow' button and Scroll Down functionality.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.verify_that_home_page_is_visible()
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.subscription.verify_text_subscription()
        self.page.evaluate("window.scrollTo(0, 0)")
        self.home_page.verify_that_home_page_is_visible()
        take_screenshot(self.page, "verify_scroll_up_without_arrow_button")