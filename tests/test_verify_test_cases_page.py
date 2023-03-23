import pytest

from pages.home_page import HomePage
from pages.verify_test_cases_page import VerifyTestCasesPage
from utils.tools import take_screenshot


class TestVerifyTestCasesPage:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.cases_page = VerifyTestCasesPage(self.page)

    def test_verify_test_cases_page(self, test_setup):
        """
        Test to verify user is navigated to test cases page successfully.
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.home_page.verify_that_home_page_is_visible()
        self.cases_page.click_test_cases_button()
        self.cases_page.verify_navigate_to_test_cases_page()
        take_screenshot(self.page, "verify_test_cases_page")
