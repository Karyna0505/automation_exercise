import pytest

from pages.home_page import HomePage
from pages.contact_us_page import ContactUs
from utils.test_data import Data
from utils.tools import take_screenshot


class TestContactUsForm:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.contact_form = ContactUs(self.page)

    def test_contact_us(self, test_setup):
        """
        Test to verify Contact Us Form.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.verify_that_home_page_is_visible()

        self.contact_form.click_contact_us_button()
        self.contact_form.check_get_in_touch_title_is_visible()
        self.contact_form.set_name(Data.username)
        self.contact_form.set_email(Data.email)
        self.contact_form.set_subject(Data.companyname)
        self.contact_form.set_message(Data.companyname)
        self.contact_form.upload_file()
        self.contact_form.click_submit_button()
        self.page.keyboard.press("Enter")
        self.contact_form.verify_success_message()
        self.contact_form.click_home_button()

        self.home_page.verify_that_home_page_is_visible()
        take_screenshot(self.page, "contact_us")
