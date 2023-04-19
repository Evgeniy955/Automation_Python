import time

from appium.webdriver.common.touch_action import TouchAction

class Functions:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def tap_on_element(self, *locator):
        self.find_element(*locator).click()

    def is_enable(self, *locator):
        self.find_element(*locator).is_enabled()

    def scroll(self, width, bottom, top):
        w = self.driver.get_window_size().get("width")
        h = self.driver.get_window_size().get("height")

        touch = TouchAction(self.driver)
        touch.press(x=w/width, y=h-bottom).move_to(x=w/width, y=top).release().perform()

    def check_text(self, expected_text, *locator):
        assert expected_text == self.find_element(*locator).text, f'Expected text: {expected_text}'

    def check_tag_name(self, expected_text, *locator):
        found_tag_name = self.find_element(*locator).tag_name
        assert expected_text == found_tag_name, f'Expected text: {found_tag_name}'

    def clear_field(self, *locator):
        self.find_element(*locator).clear()

    def value_field(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def get_url(self, url):
        self.driver.get(url)







# Scroll up
def date_picker_scroll(driver):
    w = driver.get_window_size().get("width")
    h = driver.get_window_size().get("height")

    touch = TouchAction(driver)
    touch.press(x=w / 2, y=h - 10).move_to(x=w / 2, y=10).release().perform()


# Screenshot
def save_screenshot(driver):
    ts = time.strftime("%Y_%m_%d_%H%M%S")
    activityname = driver.current_activity
    filename = activityname + ts

    driver.save_screenshot("C:/Users/halitsyn.y/PycharmProjects/trainee_Project/screenshots/" + filename + ".png")

# Restart app
def restart_app(driver):
    driver.reset()

'''Scroll down
w = driver.get_window_size().get("width")
h = driver.get_window_size().get("height")

touch = TouchAction(driver)
touch.press(x=w / 2, y=330).move_to(x=w / 2, y=h).release().perform()
'''