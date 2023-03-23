import pytest

from pages.home_page import HomePage
from pages.products_page import AllProductsPage
from pages.cart_page import CartPage
from utils.tools import take_screenshot


class TestRemoveProductFromCart:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = AllProductsPage(self.page)
        self.cart_page = CartPage(self.page)

    def test_remove_products_from_cart(self, test_setup):
        """
        Test to verify remove products from cart.
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
        self.cart_page.click_continue_shopping_button()
        self.cart_page.click_cart_button_on_header()

        self.cart_page.click_delete_product_button()
        self.cart_page.verify_that_product_is_removed_from_the_cart()
        take_screenshot(self.page, "remove_products_from_cart")
