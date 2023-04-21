from playwright.sync_api import Page, expect


class HomePage:

    def __init__(self, page: Page):

        self.page = page

        self.__home_link = self.page.locator('a[href="/"][style]')
        self.__signup_login_button = self.page.locator('li>a[href="/login"]')
        self.__cart_button = self.page.locator('li [href="/view_cart"]')
        self.__recommended_items_title = self.page.locator('[class="recommended_items"] [class="title text-center"]')
        self.__categories_on_left_side_bar = self.page.locator('[id="accordian"]')
        self.__women_category = self.page.locator('[href="#Women"]')
        self.__dress_subcategory = self.page.locator('[href="/category_products/1"]')
        self.title_page = self.page.get_by_role("heading", name="AutomationExercise")

    def verify_that_home_page_is_visible(self) -> None:
        self.__home_link.wait_for(state='visible')
        expect(self.__home_link).to_be_visible()
        expect(self.title_page).to_contain_text("AutomationExercise")

    def click_signup_login_button(self) -> None:
        self.__signup_login_button.click()

    def click_cart_button(self) -> None:
        self.__cart_button.click()

    def click_scroll_up(self) -> None:
        arrow_button = self.page.wait_for_selector('[id="scrollUp"]')
        arrow_button.click()

    def verify_recommended_items_is_visible(self) -> None:
        self.__recommended_items_title.is_visible()

    def verify_that_categories_are_visible_on_left_side_bar(self) -> None:
        self.__categories_on_left_side_bar.is_visible()

    def click_women_category(self) -> None:
        self.__women_category.click()

    def click_dress_subcategory(self) -> None:
        self.__dress_subcategory.click()

