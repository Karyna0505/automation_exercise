import allure
import pytest

from playwright.sync_api import Playwright
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.signup_form_page import SignupFormPage
from pages.personal_profile_page import PersonalProfilePage
from pages.cart_page import CartPage
from utils.test_data import Data
from utils.tools import generate_random_email

disable_loggers = []


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chromium")


@pytest.fixture(scope='function')
def new_page(playwright: Playwright, request):
    global browser
    browser_name = request.config.getoption("--browser_name")
    headless = not request.config.getoption("--headed")
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=headless)
    if browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    if browser_name == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    page.goto(f'https://automationexercise.com', timeout=60000)
    yield page
    context.close()


@pytest.fixture
def registered_user(new_page):
    page = new_page
    home_page = HomePage(page)
    signup_login = SignupLoginPage(page)
    signup_form = SignupFormPage(page)
    personal_profile = PersonalProfilePage(page)
    cart_page = CartPage(page)

    home_page.verify_that_home_page_is_visible()
    cart_page.hover_first_product()
    cart_page.click_add_to_cart_button1()
    cart_page.click_continue_shopping_button()
    cart_page.hover_second_page()
    cart_page.click_add_to_cart_button2()
    cart_page.click_continue_shopping_button()
    cart_page.click_cart_button_on_header()
    cart_page.verify_cart_page()
    cart_page.click_proceed_to_checkout_button()

    page.locator('[id="checkoutModal"] [href="/login"]').click()
    page.random_email = generate_random_email()
    signup_login.verify_new_user_title_visible()
    signup_login.enter_name(Data.username)
    signup_login.enter_email(page.random_email)
    signup_login.click_signup_button()

    signup_form.check_enter_account_information_title()
    signup_form.click_title_radio_button()
    signup_form.set_password(Data.password)
    signup_form.select_date_of_birth()
    signup_form.check_checkboxes()

    signup_form.fill_address_information(Data.firstname, Data.lastname, Data.companyname, Data.address1, Data.address2,
                                         Data.state, Data.city, Data.zipcode, Data.phonenumber)
    signup_form.click_create_account()

    signup_form.check_account_created_message()
    signup_form.click_continue_button()

    personal_profile.check_logged_in_page()


@pytest.fixture
def registered_user_logout(new_page):
    page = new_page
    home_page = HomePage(page)
    signup_login = SignupLoginPage(page)
    signup_form = SignupFormPage(page)
    personal_profile = PersonalProfilePage(page)

    home_page.verify_that_home_page_is_visible()
    home_page.click_signup_login_button()
    page.random_email = generate_random_email()
    signup_login.verify_new_user_title_visible()
    signup_login.enter_name(Data.username)
    signup_login.enter_email(page.random_email)
    signup_login.click_signup_button()

    signup_form.check_enter_account_information_title()
    signup_form.click_title_radio_button()
    signup_form.set_password(Data.password)
    signup_form.select_date_of_birth()
    signup_form.check_checkboxes()

    signup_form.fill_address_information(Data.firstname, Data.lastname, Data.companyname, Data.address1, Data.address2, Data.state, Data.city, Data.zipcode, Data.phonenumber)
    signup_form.click_create_account()

    signup_form.check_account_created_message()
    signup_form.click_continue_button()

    personal_profile.click_logout_button()


@pytest.fixture
def add_product_to_cart(new_page):
    page = new_page
    cart_page = CartPage(page)

    cart_page.hover_first_product()
    cart_page.click_add_to_cart_button1()
    cart_page.click_continue_shopping_button()
    cart_page.hover_second_page()
    cart_page.click_add_to_cart_button2()
    cart_page.click_continue_shopping_button()
    cart_page.click_cart_button_on_header()
    cart_page.verify_cart_page()
    cart_page.click_proceed_to_checkout_button()


def pytest_runtest_makereport(item, call) -> None:
    if call.when == "call":
        if call.excinfo is not None and "new_page" in item.funcargs:
            page = item.funcargs["new_page"]

            allure.attach(
                page.screenshot(full_page=True, type='png'),
                name=f"{item.nodeid}.png",
                attachment_type=allure.attachment_type.PNG
            )

