from playwright.sync_api import Page, expect


class SignupLoginPage:

    def __init__(self, page: Page):

        self.page = page

        self.__new_user_signup_title = self.page.get_by_text("New User Signup!")
        self.__input_name = self.page.locator("input[name='name']")
        self.__input_email = self.page.locator("input[data-qa='signup-email']")
        self.__signup_submit_button = self.page.locator('button[data-qa="signup-button"]')
        self.__login_to_your_account_title = self.page.get_by_text("Login to your account")
        self.__input_login_email = self.page.locator('[data-qa="login-email"]')
        self.__input_login_password = self.page.locator('[data-qa="login-password"]')
        self.__login_button = self.page.locator('button[data-qa="login-button"]')
        self.__error_message_invalid_data = self.page.get_by_text("Your email or password is incorrect!")
        self.__error_message_existing_data = self.page.get_by_text("Email Address already exist!")

    def verify_new_user_title_visible(self) -> None:
        self.__new_user_signup_title.wait_for(state='visible')
        expect(self.__new_user_signup_title).to_be_visible()

    def enter_name(self, name) -> None:
        self.__input_name.fill(name)

    def enter_email(self, email) -> None:
        self.__input_email.fill(email)

    def click_signup_button(self) -> None:
        self.__signup_submit_button.click()

    def verify_login_to_your_account_title_visible(self) -> None:
        expect(self.__login_to_your_account_title).to_be_visible()

    def enter_login_email(self, email) -> None:
        self.__input_login_email.fill(email)

    def enter_login_password(self, password) -> None:
        self.__input_login_password.fill(password)

    def click_login_button(self) -> None:
        self.__login_button.click()

    def verify_error_message_is_visible(self) -> None:
        expect(self.__error_message_invalid_data).to_be_visible()

    def verify_error_message_email_already_exist(self) -> None:
        expect(self.__error_message_existing_data).to_be_visible()

