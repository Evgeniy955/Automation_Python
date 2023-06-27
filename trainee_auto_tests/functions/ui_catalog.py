from time import sleep, time

from appium.webdriver.common.touch_action import TouchAction
from selene import be
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput




from trainee_auto_tests.functions.func import Functions
from trainee_auto_tests.locators import locators


class UiCatalogAndroid(Functions):

    @classmethod
    def tap_on_menu_framework(cls):
        cls.tap_on_element(locators.catalog_menu_framework)

    @classmethod
    def tap_on_catalog_calendar(cls):
        cls.tap_on_element(locators.catalog_calendar)

    @classmethod
    def is_enabled_calendar(cls):
        cls.is_enable(locators.calendar_enabled)

    # def date_picker_scroll(self):
    #     self.scroll(2, 10, 10)
    @classmethod
    def date_picker_scroll(cls):
        cls.scroll()

    @classmethod
    def tap_on_open_calendar(cls):
        cls.tap_on_element(locators.open_calendar)

    @classmethod
    def tap_on_date_from(cls):
        cls.tap_on_element(locators.date_from)

    @classmethod
    def tap_on_date_to(cls):
        cls.tap_on_element(locators.date_to)

    @classmethod
    def tap_on_confirm_date(cls):
        cls.tap_on_element(locators.confirm_date)

    @classmethod
    def assert_value_date(cls, expected_text):
        cls.check_text(expected_text, locators.view_date)


class CheckPrompt(Functions):

    @classmethod
    def tap_on_catalog_menu_photon(cls):
        cls.tap_on_element(locators.catalog_menu_photon)

    @classmethod
    def tap_on_dialogs(cls):
        cls.tap_on_element(locators.dialogs)

    @classmethod
    def tap_on_show_promt(cls):
        cls.tap_on_element(locators.show_promt)

    @classmethod
    def assert_header_popup_hello(cls):
        cls.check_tag_name('Hello', locators.popup_hello)

    @classmethod
    def assert_text_popup_hello(cls):
        cls.check_tag_name('Example', locators.text_example)

    @classmethod
    def clear_field_popup(cls):
        cls.clear_field(locators.field_value)

    @classmethod
    def value_insert(cls):
        cls.value_field("Test", locators.field_value)

    @classmethod
    def tap_on_close_popup_hello(cls):
        cls.tap_on_element(locators.close_popup)

    @classmethod
    def assert_header_popup_ins_value(cls):
        cls.check_tag_name('Inserted Value', locators.inserted_value_popup)

    @classmethod
    def assert_text_popup_ins_value(cls):
        cls.check_tag_name('Test', locators.value_popup)

    @classmethod
    def tap_on_close_popup_ins_value(cls):
        cls.tap_on_element(locators.close_popup)


class UiCatalogiOS(Functions):


    @classmethod
    def open_date_picker(cls):
        cls.tap_on_element(locators.catalog_calendar)

    @classmethod
    def open_calendar(cls):
        cls.tap_on_element(locators.open_calendar)

    @classmethod
    def tap_on_set_date(cls):
        cls.tap_on_element(locators.date_from)

    @classmethod
    def close_date_popup(cls):
        cls.close_popup()

    @classmethod
    def open_time_picker(cls):
        for _ in range(3):
            if cls.find_element(locators.time).matching(be.visible):
                cls.tap_on_element(locators.time)
                break
            # elif self.find_element(locator.time_new).matching(be.visible):
            #         self.tap_on_element(locator.time_new)
            #         break
            # elif self.find_element(locator.time_new_1).matching(be.visible):
            #         self.tap_on_element(locator.time_new_1)
            #         break
            print(f"Time {cls.find_element(locators.time)} is wrong" )
            # browser.element("//XCUIElementTypePickerWheel[1]")
        if not cls.find_element(locators.time).matching(be.visible):
            exit()
    @classmethod
    def close_time_picker(cls):
        '''some actions
        self.tap_on_element(locator.time) '''
        if cls.find_element(locators.time_picker_popup).matching(be.visible):
            cls.tap_on_element(locators.time)

    @classmethod
    def tap_on_confirm_date(cls):
        cls.tap_on_element(locators.confirm_date)

    @classmethod
    def assert_value_date(cls, expected_text):
        cls.check_text(expected_text, locators.view_date)
