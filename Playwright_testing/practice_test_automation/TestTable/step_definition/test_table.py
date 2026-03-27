from pytest_bdd import given, when, then, parsers, scenarios
from pages.table_page import Table

scenarios("../features/table_test.feature")

#Given

@given("practice page")
def goto_page(open_page):
    page = open_page
    page.navigate()

#When

@when(parsers.parse('user select "{lang}" language filter'))
def filter_based_on_lang(open_page, lang):
    page = open_page
    page.filter_language(lang)
@when(parsers.parse('user unchecks "{course1}" and "{course2}"'))
def uncheck_level(open_page, course1, course2):
    page = open_page
    page.uncheck_checkbox(course1, course2)
@when(parsers.parse('user choose "{enroll_range}" enrollment'))
def user_chooses_enrollment(open_page, enroll_range):
    page = open_page
    page.choose_enrollment(enroll_range)
@when(parsers.parse('user uncheck "{level}"'))
def user_uncheck_single_level(open_page, level):
    page = open_page
    page.unchecks_single_level(level)

@when(parsers.parse('user changes anything "{btn}" button appears'))
def button_appears(open_page, btn):
    page = open_page
    page.check_btn_visibility(btn)

@when(parsers.parse('click "{btn}" button'))
def click_the_visible_btn(open_page, btn):
    page = open_page
    page.click_btn(btn)

#Then

@then(parsers.parse('verify only "{lang}" language course available'))
def verify_table_based_on_lang(open_page: Table, lang):
    page = open_page
    page.filter_table_lang_based(lang)
@then(parsers.parse('verify only "{course}" course available'))
def verify_table_based_on_course(open_page, course):
    page = open_page
    page.filter_table_course_based(course)
@then(parsers.parse('verify only "{enroll_range}" or more enrollment courses available'))
def verify_enrollment_are_greater(open_page,enroll_range):
    page = open_page
    page.verify_enrollments(enroll_range)
@then(parsers.parse('the table data should consists only "{lang}", "{level}" courses with "{enroll_range}" enrollment'))
def verify_combine_filter(open_page, lang, level, enroll_range):
    page = open_page
    page.verify_combined_filters(lang, level, enroll_range)
@then(parsers.parse('user should see "{text_data}" in "{ele_id}" id element'))
def verify_text_visibility(open_page, text_data, ele_id):
    page = open_page
    page.check_text_is_visible(text_data, ele_id)
@then("verify all filters are reset")
def verify_all_values_reset(open_page):
    page = open_page
    page.check_vales_reset()
@then(parsers.parse('verify "{btn}" button is hidden'))
def verify_btn_hidden(open_page, btn):
    page = open_page
    page.check_btn_hidden(btn)