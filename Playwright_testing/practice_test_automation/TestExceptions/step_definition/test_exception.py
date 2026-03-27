from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import TimeoutError
import pytest

scenarios("../features/exceptions.feature")

#Given
#scenario [1,2,3]
@given("practice page")
def goto_page(open_page):
    page = open_page
    page.navigate()
#scenario [4]
@given(parsers.parse('the "{text_id}" text element'))
def search_instruction_text(open_page, text_id):
    page = open_page
    page.check_instruction_text_id(text_id)

#When
#scenario [1,2,3]
@when(parsers.parse('user click "{button_name}" button'))
def trigger_button(open_page, button_name):
    page = open_page
    page.trigger_given_button(button_name)
#scenario [2,3]
@when(parsers.parse('user type text "{given_text}" into "{row_num}" row'))
def insert_text_into_input(open_page, given_text, row_num):
    page = open_page
    page.insert_data_in_input_field(given_text, row_num)
#scenario [2,3]
@when(parsers.parse('user click on save button of "{row_num}" row'))
def user_clicks_save_btn(open_page, row_num):
    page = open_page
    page.click_save_btn(row_num)

#Then
#scenario [1]
@then("verify row 2 input field is displayed")
def check_new_row_displayed(open_page):
    page = open_page
    page.check_row_displayed()
#scenario [2,3]
@then(parsers.parse('verify "{given_text}" text saved on "{row_num}" row'))
def verify_test_visible(open_page, given_text, row_num):
    page = open_page
    page.verify_text_added(given_text, row_num)
#s
@then(parsers.parse('the "{text_id}" text should be invincible'))
def search_instruction_visibility(open_page, text_id):
    page = open_page
    page.check_instruction_text_visibility(text_id)

@then("wait for 3 seconds and verify second input visibility")
def verify_second_input_visibility(open_page):
    page = open_page
    with pytest.raises(AssertionError):
        page.check_row_displayed(given_timeout=3000)