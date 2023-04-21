import pytest

from pages.home_page import HomePage
from pages.products_page import AllProductsPage
from utils.tools import take_screenshot
from utils.test_data import Data


class TestVerifyProductsPage:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = AllProductsPage(self.page)

    def test_products_page(self, test_setup):
        """
        Test to verify All Products and product detail page.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.verify_that_home_page_is_visible()
        self.products_page.click_products_button()
        self.products_page.check_all_products_page_is_visible()
        assert self.page.url == f"{Data.URL}/products"
        self. products_page.check_product_list_is_visible()
        self.products_page.click_view_product_of_first_product()
        assert self.page.url == f"{Data.URL}/product_details/1"
        self.products_page.check_details_product_is_visible()
        take_screenshot(self.page, "products_page")

