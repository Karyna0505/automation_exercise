
from playwright.sync_api import Page, expect, Locator, ElementHandle
from utils.test_data import Data


class CartPage:

    def __init__(self, page: Page):

        self.page = page

        self.__add_to_cart_button1 = self.page.locator('[class="product-overlay"] [data-product-id="1"]')
        self.__first_product = self.page.locator('[src="/get_product_picture/1"]')
        self.__continue_shopping_button = self.page.locator('[id="cartModal"] button')
        self.__second_product = self.page.locator('[src="/get_product_picture/2"]')
        self.__add_to_cart_button2 = self.page.locator('[class="product-overlay"] [data-product-id="2"]')
        self.__view_cart_link = self.page.locator('p [href="/view_cart"]')
        self.__first_product_in_cart = self.page.locator('[id="product-1"]')
        self.__price_first_product = self.page.locator('[id="product-1"] [class="cart_price"]>p')
        self.__quantity_first_product = self.page.locator('[id="product-1"] [class="disabled"]')
        self.__total_price_first_product = self.page.locator('[id="product-1"] [class="cart_total_price"]')
        self.__price_second_product = self.page.locator('[id="product-2"] [class="cart_price"]>p')
        self.__quantity_second_product = self.page.locator('[id="product-2"] [class="disabled"]')
        self.__total_price_second_product = self.page.locator('[id="product-2"] [class="cart_total_price"]')
        self.__cart_button = self.page.locator('li [href="/view_cart"]')
        self.__cart_page_title = self.page.locator('[id="cart_items"] li:nth-child(2)')
        self.__proceed_to_checkout_button = self.page.locator('[class*="check_out"]')
        self.__delivery_address = self.page.locator('[id="address_delivery"]')
        self.__billing_address = self.page.locator('[id="address_invoice"]')
        self.__comment_to_order_field = self.page.locator('[class="form-control"]')
        self.__place_order_button = self.page.locator('[href="/payment"]')
        self.__delete_button = self.page.locator('[id="product-1"] [data-product-id="1"]')


    def hover_first_product(self) -> None:
        self.__first_product.hover()

    def click_add_to_cart_button1(self) -> None:
        self.__add_to_cart_button1.click()

    def click_continue_shopping_button(self) -> None:
        self.__continue_shopping_button.wait_for()
        self.__continue_shopping_button.click()

    def hover_second_page(self) -> None:
        self.__second_product.hover()

    def click_add_to_cart_button2(self) -> None:
        self.__add_to_cart_button2.click()

    def click_view_cart(self) -> None:
        self.__view_cart_link.click()

    def product1_price(self) -> float:
        return float(self.__price_first_product.inner_text().replace('Rs. ', ''))

    def product1_quantity(self) -> int:
        return int(self.__quantity_first_product.inner_text())

    def product1_total_price(self) -> float:
        return float(self.__total_price_first_product.inner_text().replace('Rs. ', ''))

    def product2_price(self) -> float:
        return float(self.__price_second_product.inner_text().replace('Rs. ', ''))

    def product2_quantity(self) -> int:
        return int(self.__quantity_second_product.inner_text())

    def product2_total_price(self) -> float:
        return float(self.__total_price_second_product.inner_text().replace('Rs. ', ''))

    def get_quantity_first_product(self) -> Locator:
        return self.__quantity_first_product

    def click_cart_button_on_header(self) -> None:
        self.__cart_button.click()

    def verify_cart_page(self) -> None:
        assert self.__cart_page_title.inner_text() == 'Shopping Cart'

    def click_proceed_to_checkout_button(self) -> None:
        self.__proceed_to_checkout_button.click()

    def verify_that_the_delivery_address_is_same_address_filled_at_the_time_registration_of_account(self) -> None:
        delivery_address = self.__delivery_address.inner_text()

        assert delivery_address == f"YOUR DELIVERY ADDRESS\nMr. {Data.firstname} {Data.lastname}\n{Data.companyname}\n{Data.address1}\n{Data.address2}\n{Data.city} {Data.state} {Data.zipcode}\nUnited States\n{Data.phonenumber}"

    def verify_that_the_billing_address_is_same_address_filled_at_the_time_registration_of_account(self) -> None:
        delivery_address = self.__billing_address.inner_text()

        assert delivery_address == f"YOUR DELIVERY ADDRESS\nMr. {Data.firstname} {Data.lastname}\n{Data.companyname}\n{Data.address1}\n{Data.address2}\n{Data.city} {Data.state} {Data.zipcode}\nUnited States\n{Data.phonenumber}"

    def enter_description_in_comment_text_area(self) -> None:
        self.__comment_to_order_field.fill(Data.searchdata)

    def click_place_order_button(self) -> None:
        self.__place_order_button.click()

    def click_delete_product_button(self) -> None:
        self.__delete_button.click()

    def verify_that_product_is_removed_from_the_cart(self) -> None:
        expect(self.__first_product_in_cart).not_to_be_visible()

    def query_selector_all(self) -> list[ElementHandle]:
        return self.page.query_selector_all('tbody>tr')

    def get_delivery_address(self) -> Locator:
        return self.page.locator('[id="address_delivery"]')

    def get_billing_address_text(self) -> Locator:
        return self.page.locator('[id="address_invoice"]')

    def query_selector_all_products(self) -> list[ElementHandle]:
        return self.page.query_selector_all('tr[id*="product-"]')