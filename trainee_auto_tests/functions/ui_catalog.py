from trainee_auto_tests.functions.func import Functions
from trainee_auto_tests.locators import locator


class UiCatalog(Functions):

    def __init__(self, mobile):
        super().__init__(mobile)

    def tap_on_menu_framework(self):
        self.tap_on_element(locator.catalog_menu_framework)

    def tap_on_catalog_calendar(self):
        self.tap_on_element(locator.catalog_calendar)

    def is_enabled_calendar(self):
        self.is_enable(locator.calendar_enabled)

    # def date_picker_scroll(self):
    #     self.scroll(2, 10, 10)

    def date_picker_scroll(self):
        self.scroll()

    def tap_on_open_calendar(self):
        self.tap_on_element(locator.open_calendar)

    def tap_on_date_from(self):
        self.tap_on_element(locator.date_from)

    def tap_on_date_to(self):
        self.tap_on_element(locator.date_to)

    def tap_on_confirm_date(self):
        self.tap_on_element(locator.confirm_date)

    def assert_value_date(self, expected_text):
        self.check_text(expected_text, locator.view_date)


class CheckPrompt(Functions):

    def __init__(self, driver):
        super().__init__(driver)

    def tap_on_catalog_menu_photon(self):
        self.tap_on_element(locator.catalog_menu_photon)

    def tap_on_dialogs(self):
        self.tap_on_element(locator.dialogs)

    def tap_on_show_promt(self):
        self.tap_on_element(locator.show_promt)

    def assert_header_popup_hello(self):
        self.check_tag_name('Hello', locator.popup_hello)

    def assert_text_popup_hello(self):
        self.check_tag_name('Example', locator.text_example)

    def clear_field_popup(self):
        self.clear_field(locator.field_value)

    def value_insert(self):
        self.value_field("Test", locator.field_value)

    def tap_on_close_popup_hello(self):
        self.tap_on_element(locator.close_popup)

    def assert_header_popup_ins_value(self):
        self.check_tag_name('Inserted Value', locator.inserted_value_popup)

    def assert_text_popup_ins_value(self):
        self.check_tag_name('Test', locator.value_popup)

    def tap_on_close_popup_ins_value(self):
        self.tap_on_element(locator.close_popup)
