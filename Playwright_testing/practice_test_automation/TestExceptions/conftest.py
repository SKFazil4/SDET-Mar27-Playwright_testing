from playwright.sync_api import Playwright
import pytest
from pages.exception_page import ExceptionPage

@pytest.fixture
def create_browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()

@pytest.fixture
def open_page(create_browser):
    page = create_browser
    test_page = ExceptionPage(page)
    yield test_page