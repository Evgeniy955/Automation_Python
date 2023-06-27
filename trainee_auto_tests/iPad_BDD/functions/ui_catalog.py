from time import sleep, time

from appium.webdriver.common.touch_action import TouchAction
from selene import be
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from trainee_auto_tests.iPad_BDD.functions.func import Functions
from trainee_auto_tests.iPad_BDD.locators import locators


class UiCatalogiPad(Functions):

    @classmethod
    def uicatalog_should_be_opened(cls):
        cls.tap_on_element(locators.catalog_calendar)

    @classmethod
    def open_date_picker_iPad(cls):
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
