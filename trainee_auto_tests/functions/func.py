import time
from datetime import datetime
from time import sleep

from selene.support.shared import browser
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selene.core import query
from selene.support.conditions import be


class Functions:

    @staticmethod
    def find_element(locator):
        return browser.element(locator)

    @classmethod
    def tap_on_element(cls,locator):
        cls.find_element(locator).click()

    @classmethod
    def is_enable(cls, locator):
        cls.find_element(locator).matching(be.enabled)
        # self.find_element(locator).is_enabled()

    @staticmethod
    def scroll():
        w = browser.driver.get_window_size().get("width")
        h = browser.driver.get_window_size().get("height")

        for scroll in range(2):
            actions = ActionChains(browser.driver)
            actions.w3c_actions = ActionBuilder(browser.driver,
                                                mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(w / 2, h - 10)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(w / 2, h/4)
            actions.perform()

    @staticmethod
    def close_popup():
        w = browser.driver.get_window_size().get("width")
        h = browser.driver.get_window_size().get("height")
        actions = ActionChains(browser.driver)
        actions.w3c_actions = ActionBuilder(browser.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(w / 2, h / 4)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    @classmethod
    def check_text(cls, expected_text, locator):
        assert expected_text == cls.find_element(locator).get(query.text), f'Expected text: {expected_text}'

    @classmethod
    def check_tag_name(cls, expected_text, locator):
        found_tag_name = cls.find_element(locator).get(query.tag)
        assert expected_text == found_tag_name, f'Expected text: {found_tag_name}'

    @classmethod
    def clear_field(cls, locator):
        cls.find_element(locator).clear()

    @classmethod
    def value_field(cls, text, locator):
        cls.find_element(locator).send_keys(text)

    @staticmethod
    def get_url(url):
        browser.driver.get(url)

    @staticmethod
    def time():
        server_time = datetime.now().strftime("%H:%M:%S")
        time = server_time[-8:-3]
        minute = int(time[-1])
        if minute == 0:
            minute = 1
        time_new = time.replace(time[-1], str(minute - 1))
        time_new_2 = time.replace(time[-1], str(minute + 1))
        return time,time_new,time_new_2



# Screenshot
    @staticmethod
    def save_screenshot(driver):
        ts = time.strftime("%Y_%m_%d_%H%M%S")
        activityname = driver.current_activity
        filename = activityname + ts

        driver.save_screenshot("C:/Users/halitsyn.y/PycharmProjects/Automation/trainee_auto_tests/screenshots" + filename + ".png")


# Restart app
    @staticmethod
    def restart_app(driver):
        driver.reset()


    @staticmethod
    def open_menu():
        w = browser.driver.get_window_size().get("width")
        h = browser.driver.get_window_size().get("height")
        actions = ActionChains(browser.driver)
        actions.w3c_actions = ActionBuilder(browser.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(w / 54, h / 2)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(w / 3, h / 2)
        actions.w3c_actions.pointer_action.release()
        actions.perform()


    @staticmethod
    def close_menu():
        w = browser.driver.get_window_size().get("width")
        h = browser.driver.get_window_size().get("height")
        actions = ActionChains(browser.driver)
        actions.w3c_actions = ActionBuilder(browser.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(w / 1.5, h / 2)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

'''Scroll down
w = driver.get_window_size().get("width")
h = driver.get_window_size().get("height")

touch = TouchAction(driver)
touch.press(x=w / 2, y=330).move_to(x=w / 2, y=h).release().perform()
'''

time_now = Functions.time()