from playwright.sync_api import Playwright
import pytest
from pages.table_page import Table


@pytest.fixture
def browser_create(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()

@pytest.fixture
def open_page(browser_create):
    page = browser_create
    table_page = Table(page)
    yield table_page
