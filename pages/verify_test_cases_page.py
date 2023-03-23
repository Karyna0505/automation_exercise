from playwright.sync_api import Page, expect


class VerifyTestCasesPage:

    def __init__(self, page: Page):

        self.page = page

        self.__button_test_cases = self.page.locator('header a[href="/test_cases"]')
        self.__title_test_cases = self.page.locator('h2 b')
        self.__case1 = self.page.locator('[href="#collapse1"]')

    def click_test_cases_button(self) -> None:
        self.__button_test_cases.click()

    def verify_navigate_to_test_cases_page(self) -> None:
        self.__title_test_cases.is_visible()

