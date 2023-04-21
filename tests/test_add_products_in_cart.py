import pytest

from pages.home_page import HomePage
from pages.products_page import AllProductsPage
from pages.cart_page import CartPage
from utils.tools import take_screenshot


class TestAddProductsInCart:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = AllProductsPage(self.page)
        self.cart_page = CartPage(self.page)

    def test_add_products_in_cart(self, test_setup):
        """
        Test to verify Add Products in Cart.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.verify_that_home_page_is_visible()
        self.products_page.click_products_button()

        self.cart_page.hover_first_product()
        self.cart_page.click_add_to_cart_button1()
        self.cart_page.click_continue_shopping_button()
        self.cart_page.hover_second_page()
        self.cart_page.click_add_to_cart_button2()
        self.cart_page.click_view_cart()

        assert len(self.cart_page.query_selector_all()) == 2

        assert self.cart_page.product1_total_price() == self.cart_page.product1_price() * self.cart_page.product1_quantity()

        assert self.cart_page.product2_total_price() == self.cart_page.product2_price() * self.cart_page.product2_quantity()
        take_screenshot(self.page, "add_product_in_cart")

