from functions.func import Functions
from time import sleep

from locators import locator


class Byiphone(Functions):

    def __init__(self, driver):
        super().__init__(driver)

    def url_address(self):
        self.get_url('https://www.apple.com/iphone/buy')

    def click_iphone13pro(self):
        self.tap_on_element(*locator.iphone13pro)

    def click_buy_button(self):
        self.tap_on_element(*locator.buy_button)

    def click_iphone13pro_max(self):
        self.tap_on_element(*locator.iphone13pro_max)
        sleep(1)

    def click_color(self):
        self.tap_on_element(*locator.color)
        sleep(1)

    def click_memory_device(self):
        self.tap_on_element(*locator.memory_device)
        sleep(1)

    def click_connect_later(self):
        self.tap_on_element(*locator.connect_later)

    def click_no_smartphone_to_trade(self):
        self.tap_on_element(*locator.no_smartphone_to_trade)
        sleep(1)

    def click_payment_option(self):
        self.tap_on_element(*locator.payment_option)
        sleep(1)

    def click_one_time_payment(self):
        self.tap_on_element(*locator.one_time_payment)

    def click_add_to_bag(self):
        self.tap_on_element(*locator.add_to_bag)

    def assert_bag(self):
        self.check_text('iPhone 13 Pro Max 512GB Silver', *locator.review_bag)
