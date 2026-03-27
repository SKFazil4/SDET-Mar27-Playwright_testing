from playwright.sync_api import expect

class ExceptionPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://practicetestautomation.com/practice-test-exceptions/")

    def trigger_given_button(self, button_name):
        self.page.get_by_role("button", name=button_name).click()

    def check_row_displayed(self, given_timeout = 6000):
        expect(self.page.locator("#row2")).to_be_visible(timeout=given_timeout)

    def insert_data_in_input_field(self, given_text, row_num):
        row = self.page.locator(f"#{row_num}")
        row.locator(".input-field").fill(given_text)

    def click_save_btn(self, row_num):
        row = self.page.locator(f"#{row_num}")
        row.locator("#save_btn").click()

    def verify_text_added(self,given_text, row_num):
        row = self.page.locator(f"#{row_num}")
        expect(row.locator(".input-field")).to_have_value(given_text)

    def check_instruction_text_id(self, text_id):
        expect(self.page.locator(f"#{text_id}")).to_be_visible()

    def check_instruction_text_visibility(self, text_id):
        expect(self.page.locator(f"#{text_id}")).not_to_be_visible()
        self.page.wait_for_timeout(3000)
