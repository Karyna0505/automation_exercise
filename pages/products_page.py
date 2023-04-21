from playwright.sync_api import Page, expect


class AllProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.__products_button = self.page.locator('[href="/products"]')
        self.__all_products_title = self.page.locator('[class="title text-center"]')
        self.__product_list = self.page.locator('[class="features_items"]')
        self.__view_product1 = self.page.locator('[href="/product_details/1"]')
        self.__product_name = self.page.get_by_text("Blue Top")
        self.__category_product = self.page.get_by_text("Category: Women > Tops")
        self.__price_product = self.page.locator('span>span')
        self.__availability = self.page.get_by_text("Availability:")
        self.__condition = self.page.get_by_text("Condition:")
        self.__brand = self.page.get_by_text("Brand:")
        self.__quantity_filed = self.page.locator('[id="quantity"]')
        self.__add_to_cart_button = self.page.locator('[type="button"]')
        self.__product_information = self.page.locator('[class="product-information"]')
        self.__add_to_cart_button_recommended = self.page.locator(
            '[id="recommended-item-carousel"] [data-product-id="4"]')
        self.__category_title_page = self.page.locator('[class="features_items"] h2[class="title text-center"]')
        self.__men_category = self.page.locator('[href="#Men"]')
        self.__tshirt_subcategory = self.page.locator('[href="/category_products/3"]')
        self.__brand_on_the_left_side_bar = self.page.locator('[class="brands_products"]')
        self.__polo_brand = self.page.locator('[href="/brand_products/Polo"]')
        self.__biba_brand = self.page.locator('[href="/brand_products/Biba"]')

    def click_products_button(self) -> None:
        self.__products_button.click()

    def check_all_products_page_is_visible(self) -> None:
        self.__all_products_title.is_visible()

    def check_product_list_is_visible(self) -> None:
        self.__product_list.is_visible()

    def click_view_product_of_first_product(self) -> None:
        self.__view_product1.click()

    def check_details_product_is_visible(self) -> None:
        self.__product_name.is_visible()
        self.__category_product.is_visible()
        self.__price_product.is_visible()
        self.__availability.is_visible()
        self.__condition.is_visible()
        self.__brand.is_visible()

    def increase_quantity_to_4(self) -> None:
        self.__quantity_filed.fill('')
        self.__quantity_filed.fill('4')

    def click_add_to_cart_button(self) -> None:
        self.__add_to_cart_button.click()

    def verify_product_detail_is_opened(self) -> None:
        self.__product_information.is_visible()

    def click_add_to_cart_button_recommended(self) -> None:
        self.__add_to_cart_button_recommended.click()

    def verify_that_category_page_is_displayed(self) -> None:
        self.__category_title_page.is_visible()

    def click_subcategory_from_men_category(self) -> None:
        self.__men_category.click()
        self.__tshirt_subcategory.click()

    def check_women_dress_title(self) -> None:
        expect(self.__category_title_page).to_contain_text("Women - Dress")

    def check_men_tshirts_title(self) -> None:
        expect(self.__category_title_page).to_contain_text("Men - Tshirts")

    def verify_brands_visible_on_left_side_bar(self) -> None:
        self.__brand_on_the_left_side_bar.is_visible()

    def click_polo_brand(self) -> None:
        self.__polo_brand.click()

    def click_biba_brand(self) -> None:
        self.__biba_brand.click()
