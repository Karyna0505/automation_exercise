import pytest

from pages.home_page import HomePage
from pages.products_page import AllProductsPage
from utils.tools import take_screenshot


class TestViewCategoryProducts:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = AllProductsPage(self.page)

    def test_view_category_products(self, test_setup):
        """
        Test to verify View Category Products.
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.verify_that_categories_are_visible_on_left_side_bar()
        self.home_page.click_women_category()
        self.home_page.click_dress_subcategory()
        self.products_page.verify_that_category_page_is_displayed()
        self.products_page.check_women_dress_title()
        self.products_page.click_subcategory_from_men_category()
        self.products_page.verify_that_category_page_is_displayed()
        self.products_page.check_men_tshirts_title()
        take_screenshot(self.page, "view_category_products")
