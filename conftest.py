import allure
import pytest

from playwright.sync_api import Playwright

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
    page.goto(f'https://automationexercise.com')
    yield page
    context.close()


def pytest_runtest_makereport(item, call) -> None:
    if call.when == "call":
        if call.excinfo is not None and "new_page" in item.funcargs:
            page = item.funcargs["new_page"]

            allure.attach(
                page.screenshot(full_page=True, type='png'),
                name=f"{item.nodeid}.png",
                attachment_type=allure.attachment_type.PNG
            )
