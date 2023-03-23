import pytest

from pages.home_page import HomePage
from pages.search_product_page import SearchProduct
from pages.products_page import AllProductsPage
from utils.test_data import Data
from utils.tools import take_screenshot


class TestSearchProduct:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.search_product = SearchProduct(self.page)
        self.products_page = AllProductsPage(self.page)

    def test_search_product(self, test_setup):
        """
        Test to verify search product.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.verify_that_home_page_is_visible()
        self.products_page.click_products_button()

        self.products_page.check_all_products_page_is_visible()
        assert self.page.url == 'https://automationexercise.com/products'

        self.search_product.set_data_in_search_field(Data.searchdata)
        self.search_product.click_search_button()
        self.search_product.verify_searched_product_title_is_visible()
        self.search_product.verify_all_products_related_to_search_are_visible()
        take_screenshot(self.page, "search_product")



