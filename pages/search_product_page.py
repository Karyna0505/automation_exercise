from playwright.sync_api import Page


class SearchProduct:

    def __init__(self, page: Page):

        self.page = page

        self.__input_search_field = self.page.locator('input[id="search_product"]')
        self.__search_button = self.page.locator('[id="submit_search"]')
        self.__searched_product_title = self.page.locator('[class="title text-center"]')
        self.__first_product = self.page.locator('[src="/get_product_picture/28"]')
        self.__second_product = self.page.locator('[src="/get_product_picture/29"]')
        self.__add_to_cart_button1 = self.page.locator('[class="product-overlay"] [data-product-id="28"]')
        self.__add_to_cart_button2 = self.page.locator('[class="product-overlay"] [data-product-id="29"]')

    def set_data_in_search_field(self, data) -> None:
        self.__input_search_field.fill(data)

    def click_search_button(self) -> None:
        self.__search_button.click()

    def verify_searched_product_title_is_visible(self) -> None:
        self.__searched_product_title.is_visible()

    def verify_all_products_related_to_search_are_visible(self) -> None:
        products = self.page.query_selector_all('.product')
        for product in products:
            assert 't-shirt' in product.text_content().lower()

    def hover_first_product(self) -> None:
        self.__first_product.hover()

    def hover_second_product(self) -> None:
        self.__second_product.hover()

    def click_add_to_cart_button1(self) -> None:
        self.__add_to_cart_button1.click()

    def click_add_to_cart_button2(self) -> None:
        self.__add_to_cart_button2.click()

    def verify_first_product_is_visible(self) -> None:
        self.__first_product.is_visible()

    def verify_second_product_is_visible(self) -> None:
        self.__second_product.is_visible()