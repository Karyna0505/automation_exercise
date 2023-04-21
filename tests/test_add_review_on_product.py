import pytest

from pages.home_page import HomePage
from pages.products_page import AllProductsPage
from pages.review_page import ReviewForm
from utils.test_data import Data
from utils.tools import take_screenshot


class TestAddReviewOnProduct:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = AllProductsPage(self.page)
        self.review_page = ReviewForm(self.page)

    def test_add_review_on_product(self, test_setup):
        """
        Test to verify Add review on product.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.products_page.click_products_button()
        self.products_page.check_all_products_page_is_visible()
        assert self.page.url == f"{Data.URL}/products"
        self.products_page.click_view_product_of_first_product()
        self.review_page.verify_write_review_title()
        self.review_page.set_name_email_review(Data.username, Data.email, Data.companyname)
        self.review_page.click_submit_button()
        self.review_page.verify_success_message()
        take_screenshot(self.page, "add_review_on_product")
