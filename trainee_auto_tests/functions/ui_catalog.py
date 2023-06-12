from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selene import be
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from functions.func import Functions
from locators import locator


class UiCatalogAndroid(Functions):

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


class UiCatalogiOS(Functions):

    def __init__(self, mobile):
        super().__init__(mobile)

    def open_date_picker(self):
        self.tap_on_element(locator.catalog_calendar)

    def open_calendar(self):
        self.tap_on_element(locator.open_calendar)

    def tap_on_set_date(self):
        self.tap_on_element(locator.date_from)

    def close_date_popup(self):
        actions = ActionChains(self.mobile.driver)
        actions.w3c_actions = ActionBuilder(self.mobile.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(169, 200)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def open_time_picker(self):
        for _ in range(3):
            if self.find_element(locator.time).matching(be.visible):
                self.tap_on_element(locator.time)
                break
            # browser.element("//XCUIElementTypePickerWheel[1]")

    def close_time_picker(self):
        '''some actions
        self.tap_on_element(locator.time) '''
        if self.find_element(locator.time_picker_popup).matching(be.visible):
            self.tap_on_element(locator.time)

    def tap_on_confirm_date(self):
        self.tap_on_element(locator.confirm_date)

    def assert_value_date(self, expected_text):
        self.check_text(expected_text, locator.view_date)
