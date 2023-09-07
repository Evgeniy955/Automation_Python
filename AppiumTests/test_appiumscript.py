from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import Browser, Config, by
from selene.core import query
from selene.support.shared import browser
from selenium.webdriver.common.by import By

# desired_capabilities ={
#     'platformName': "Android",
#     'platformVersion': "13",
#     'deviceName': "9A191FFAZ004MA",
#     'appPackage': "org.wikipedia",
#     'appActivity': "org.wikipedia.main.MainActivity",
#     'app': "C:\\Users\\halitsyn.y\\PycharmProjects\\Automation_Python\\AppiumTests\\app_wiki\\wikipedia_2.7.50398.apk"

options_catalog = UiAutomator2Options()
options_catalog.platform_name = "Android"
options_catalog.platform_version = "13"
options_catalog.device_name = "9A191FFAZ004MA"
# options_catalog.device_name = "Android Emulator"
options_catalog.app_package = "org.wikipedia"
options_catalog.app_activity = "org.wikipedia.main.MainActivity"
options_catalog.app = "/Users/halitsy.y/PycharmProjects/Automation_Python/AppiumTests/app_wiki/wikipedia_2.7.50398.apk"

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities), timeout=5,


browser_instance = Browser(Config(
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options_catalog),
    timeout=20,
    ))
browser.config.driver = browser_instance.driver


def test_wiki():
    browser.element(by.id('org.wikipedia:id/search_container')).click()
    # driver.find_element(By.ID, 'org.wikipedia:id/search_container').click()

    e = browser.element(by.id("org.wikipedia:id/search_src_text"))
    # e = driver.find_element(By.ID, "org.wikipedia:id/search_src_text")
    e.clear()
    e.send_keys("Python")

    # text = driver.find_element(By.ID, 'org.wikipedia:id/page_list_item_title').text
    text = browser.element(by.id('org.wikipedia:id/page_list_item_title')).get(query.text)

    assert 'Python' in text, f'Expected Python to be {text}'

test_wiki()