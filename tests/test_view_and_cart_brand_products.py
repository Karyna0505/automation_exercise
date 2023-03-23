import pytest

from pages.home_page import HomePage
from pages.products_page import AllProductsPage
from utils.tools import take_screenshot


class TestViewAndCartBrandProducts:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = AllProductsPage(self.page)

    def test_view_and_cart_brand_products(self, test_setup):
        """
        Test to verify View & Cart Brand Products.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.verify_that_home_page_is_visible()
        self.products_page.click_products_button()
        self.products_page.verify_brands_visible_on_left_side_bar()
        self.products_page.click_polo_brand()
        assert 'Polo' in self.page.url
        self.products_page.check_all_products_page_is_visible()
        self.products_page.click_biba_brand()
        assert 'Biba' in self.page.url
        self.products_page.check_all_products_page_is_visible()
        take_screenshot(self.page, "view_and_cart_brand_products")
