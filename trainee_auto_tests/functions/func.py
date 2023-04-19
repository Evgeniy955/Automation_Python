import time
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selene.core import query
from selene.support.conditions import be


class Functions:

    def __init__(self, mobile):
        self.mobile = mobile

    def find_element(self, locator):
        return self.mobile.element(locator)

    def tap_on_element(self, locator):
        self.find_element(locator).click()

    def is_enable(self, locator):
        self.find_element(locator).matching(be.enabled)
        # self.find_element(locator).is_enabled()

    def scroll(self):
        w = self.mobile.driver.get_window_size().get("width")
        h = self.mobile.driver.get_window_size().get("height")

        for scroll in range(2):
            actions = ActionChains(self.mobile.driver)
            actions.w3c_actions = ActionBuilder(self.mobile.driver,
                                                mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(w / 2, h - 10)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(w / 2, h/4)
            actions.perform()


    def check_text(self, expected_text, locator):
        assert expected_text == self.find_element(locator).get(query.text), f'Expected text: {expected_text}'

    def check_tag_name(self, expected_text, locator):
        found_tag_name = self.find_element(locator).get(query.tag)
        assert expected_text == found_tag_name, f'Expected text: {found_tag_name}'

    def clear_field(self, locator):
        self.find_element(locator).clear()

    def value_field(self, text, locator):
        self.find_element(locator).send_keys(text)

    def get_url(self, url):
        self.mobile.driver.get(url)



# Screenshot
def save_screenshot(driver):
    ts = time.strftime("%Y_%m_%d_%H%M%S")
    activityname = driver.current_activity
    filename = activityname + ts

    driver.save_screenshot("C:\\Users\\Yevhen\\PycharmProjects\\trainee_auto_tests\\screenshots" + filename + ".png")


# Restart app
def restart_app(driver):
    driver.reset()


'''Scroll down
w = driver.get_window_size().get("width")
h = driver.get_window_size().get("height")

touch = TouchAction(driver)
touch.press(x=w / 2, y=330).move_to(x=w / 2, y=h).release().perform()
'''
