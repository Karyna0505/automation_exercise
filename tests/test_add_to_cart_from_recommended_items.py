import pytest

from pages.home_page import HomePage
from pages.products_page import AllProductsPage
from pages.cart_page import CartPage
from utils.tools import take_screenshot


class TestRecommendedItems:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = AllProductsPage(self.page)
        self.cart_page = CartPage(self.page)

    def test_add_to_cart_recommended_product(self, test_setup):
        """
        Test to Add to cart from Recommended items.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.verify_that_home_page_is_visible()
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.home_page.verify_recommended_items_is_visible()
        self.products_page.click_add_to_cart_button_recommended()
        self.cart_page.click_view_cart()
        assert len(self.cart_page.query_selector_all()) == 1

        take_screenshot(self.page, "add_to_cart_from_recommended")
