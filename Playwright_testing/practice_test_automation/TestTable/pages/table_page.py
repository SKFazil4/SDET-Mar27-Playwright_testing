from playwright.sync_api import Page, expect

class Table:
    def __init__(self, page:Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://practicetestautomation.com/practice-test-table/")

    def filter_language(self, lang):
        self.page.get_by_role("radio",name= f"{lang}").click()

    def filter_table_lang_based(self, lang):
        headers = self.page.locator("th")
        lang_col = None
        for index in range (headers.count()):
            if headers.nth(index).inner_text().strip() == "Language":
                lang_col = index
                break

        rows = self.page.locator("tbody tr:visible")

        for i in range(rows.count()):
            row = rows.nth(i)
            cell_text = row.locator("td").nth(lang_col).inner_text()
            assert cell_text == lang

    def uncheck_checkbox(self, level1, level2):
        self.page.get_by_role("checkbox", name=level1).click()
        self.page.get_by_role("checkbox", name=level2).click()

    def filter_table_course_based(self, course):
        headers = self.page.locator("th")
        course_col = None
        for index in range (headers.count()):
            if headers.nth(index).inner_text().strip() == "Level":
                course_col = index
                break

        rows = self.page.locator("tbody tr:visible")

        for i in range(rows.count()):
            row = rows.nth(i)
            cell_text = row.locator("td").nth(course_col).inner_text()
            assert cell_text == course

    def choose_enrollment(self, enroll_range):
        # Open dropdown
        self.page.locator("#enrollDropdown .dropdown-button").click()

        # Select option
        self.page.get_by_role("option", name=enroll_range).click()

    def verify_enrollments(self, enroll_range):
        headers = self.page.locator("th")
        enroll_col = None
        for index in range(headers.count()):
            if headers.nth(index).inner_text().strip() == "Enrollments":
                enroll_col = index
                break

        rows = self.page.locator("tbody tr:visible")

        for i in range(rows.count()):
            row = rows.nth(i)
            cell_text = row.locator("td").nth(enroll_col).inner_text()
            assert cell_text >= enroll_range

    def verify_combined_filters(self, lang, level, enroll_range):
        headers = self.page.locator("th")
        enroll_col = None
        lang_col = None
        level_col = None
        for index in range(headers.count()):
            if headers.nth(index).inner_text().strip() == "Enrollments":
                enroll_col = index
            elif headers.nth(index).inner_text().strip() == "Level":
                level_col = index
            elif headers.nth(index).inner_text().strip() == "Language":
                lang_col = index

        rows = self.page.locator("tbody tr:visible")

        for i in range(rows.count()):
            row = rows.nth(i)
            level_cell_text = row.locator("td").nth(level_col).inner_text()
            lang_cell_text = row.locator("td").nth(lang_col).inner_text()
            enroll_cell_text = row.locator("td").nth(enroll_col).inner_text()
            assert enroll_cell_text >= enroll_range
            assert lang_cell_text >= lang
            assert level_cell_text >= level

    def unchecks_single_level(self,level):
        self.page.get_by_role("checkbox", name=level).click()

    def check_text_is_visible(self, text_data, ele_id):
        expect(self.page.locator(f"#{ele_id}")).to_contain_text(text_data)

    def check_btn_visibility(self, btn):
        expect(self.page.locator("#resetFilters")).to_contain_text(btn)

    def click_btn(self, btn):
        self.page.get_by_role("button",name=btn).click()

    def check_vales_reset(self):
        expect(self.page.get_by_role("radio", name="Any")).to_be_checked()
        expect(self.page.get_by_role("checkbox", name="Beginner")).to_be_checked()
        expect(self.page.get_by_role("checkbox", name="Intermediate")).to_be_checked()
        expect(self.page.get_by_role("checkbox", name="Advanced")).to_be_checked()
        expect(self.page.locator(".dropdown-label")).to_contain_text("Any")

    def check_btn_hidden(self, btn):
        expect(self.page.get_by_role("button", name=btn)).to_be_hidden()