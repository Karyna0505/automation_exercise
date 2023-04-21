import pytest


from pages.home_page import HomePage
from pages.products_page import AllProductsPage
from pages.cart_page import CartPage
from utils.tools import take_screenshot


class TestQuantityInCart:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = AllProductsPage(self.page)
        self.cart_page = CartPage(self.page)

    def test_product_quantity_in_cart(self, test_setup):
        """
        Test to verify Product quantity in Cart
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.verify_that_home_page_is_visible()
        self.products_page.click_view_product_of_first_product()
        self.products_page.verify_product_detail_is_opened()
        self.products_page.increase_quantity_to_4()
        self.products_page.click_add_to_cart_button()
        self.cart_page.click_view_cart()
        quantity_element = self.cart_page.get_quantity_first_product()
        quantity_text = quantity_element.inner_text()
        assert quantity_text == '4'
        take_screenshot(self.page, "verify_product_quantity_in_cart")

