import pytest


from func_app.func import save_screenshot
from locators import locator
from time import sleep

url_apple = ('https://www.apple.com/iphone/buy')

@pytest.mark.which_app("buyiphone")
def test_buyiphone(driver):
    driver.implicitly_wait(20)
    driver.get(url_apple)
    driver.find_element(*locator.iphone13pro).click()
    driver.find_element(*locator.buy_button).click()
    driver.find_element(*locator.iphone13pro_max).click()
    sleep(1)
    driver.find_element(*locator.color).click()
    sleep(1)
    driver.find_element(*locator.memory_device).click()
    sleep(1)
    driver.find_element(*locator.connect_later).click()
    driver.find_element(*locator.no_smartphone_to_trade).click()
    sleep(1)
    driver.find_element(*locator.payment_option).click()
    driver.find_element(*locator.one_time_payment).click()
    driver.find_element(*locator.add_to_bag).click()

    save_screenshot(driver)

    item_card = driver.find_element(*locator.review_bag).text

    assert 'iPhone 13 Pro Max 512GB Silver' in item_card, f'Expected Python to be: {item_card}'

