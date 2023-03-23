from playwright.sync_api import Page


class SignupFormPage:

    def __init__(self, page: Page):

        self.page = page

        self.__enter_account_information_title = self.page.get_by_text("Enter Account Information")
        self.__mr_title = self.page.locator('input[id="id_gender1"]')
        self.__input_password = self.page.locator('input[id="password"]')
        self.__day_birth_dropdown = self.page.locator('select[id="days"]')
        self.__month_birth_dropdown = self.page.locator('select[id="months"]')
        self.__year_birth_dropdown = self.page.locator('select[id="years"]')
        self.__newsletter_checkbox = self.page.locator('input[id="newsletter"]')
        self.__special_offers_checkbox = self.page.locator('input[id="optin"]')
        self.__input_firstname = self.page.locator('[id="first_name"]')
        self.__input_lastname = self.page.locator('[id="last_name"]')
        self.__input_company = self.page.locator('[id="company"]')
        self.__input_address1 = self.page.locator('[id="address1"]')
        self.__input_address2 = self.page.locator('[id="address2"]')
        self.__country_dropdown = self.page.locator('[id="country"]')
        self.__input_state = self.page.locator('[id="state"]')
        self.__input_city = self.page.locator('[id="city"]')
        self.__input_zipcode = self.page.locator('[id="zipcode"]')
        self.__input_mobile_number = self.page.locator('[id="mobile_number"]')
        self.__create_account_button = self.page.locator('//button[text()="Create Account"]')
        self.__successful_message_title = self.page.get_by_text("Account Created!")
        self.__continue_button = self.page.locator('a[data-qa="continue-button"]')

    def check_enter_account_information_title(self) -> None:
        self.__enter_account_information_title.wait_for(state='visible')

    def click_title_radio_button(self) -> None:
        self.__mr_title.check()

    def set_password(self, password) -> None:
        self.__input_password.fill(password)

    def select_date_of_birth(self) -> None:
        self.__day_birth_dropdown.select_option("3", force=True)
        self.__month_birth_dropdown.select_option("June", force=True)
        self.__year_birth_dropdown.select_option("1994", force=True)

    def check_checkboxes(self) -> None:
        self.__newsletter_checkbox.check()
        self.__special_offers_checkbox.check()

    def fill_address_information(self, name, lastname, companyname, address1, address2, state, city, zipcode, phone) -> None:
        self.__input_firstname.fill(name)
        self.__input_lastname.fill(lastname)
        self.__input_company.fill(companyname)
        self.__input_address1.fill(address1)
        self.__input_address2.fill(address2)
        self.__country_dropdown.select_option("United States", force=True)
        self.__input_state.fill(state)
        self.__input_city.fill(city)
        self.__input_zipcode.fill(zipcode)
        self.__input_mobile_number.fill(phone)

    def click_create_account(self) -> None:
        self.__create_account_button.click()

    def check_account_created_message(self) -> None:
        self.__successful_message_title.wait_for(state='visible')

    def click_continue_button(self) -> None:
        self.__continue_button.click()

    

