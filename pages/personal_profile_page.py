from playwright.sync_api import Page, expect
from utils.test_data import Data


class PersonalProfilePage:

    def __init__(self, page: Page):

        self.page = page

        self.__logged_in_page = self.page.get_by_text(" Logged in as ")
        self.__delete_account_link = self.page.locator('[href="/delete_account"]')
        self.__successful_deleted_account_title = self.page.get_by_text("Account Deleted!")
        self.__continue2_button = self.page.locator('a[data-qa="continue-button"]')
        self.__logout_button = self.page.locator('[href="/logout"]')

    def check_logged_in_page(self) -> None:
        expect(self.__logged_in_page).to_contain_text(Data.username)

    def click_delete_account_link(self) -> None:
        self.__delete_account_link.click()

    def verify_successful_deleted_account(self) -> None:
        expect(self.__successful_deleted_account_title).to_be_visible()

    def click_continue2_button(self) -> None:
        self.__continue2_button.click()

    def click_logout_button(self) -> None:
        self.__logout_button.click()



