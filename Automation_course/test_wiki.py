from appium import webdriver
from selene import by, be, have, Browser, Config
# from selene.api import *
from selene.support.shared import browser
import pytest
from selenium.webdriver.chrome.options import Options
from selene.core import query
from appium.options.android import UiAutomator2Options

# desired_capabilities = {
#     'platformName': "Android",
#     'platformVersion': "11",
#     'deviceName': "Android Emulator",
#     'app': "C:/Users/halitsyn.y/PycharmProjects/AppiumTests/app_wiki/wikipedia_2.7.50398.apk"
# }
#
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
# mobile = Browser(Config(
#     driver=driver,
#     timeout=10))

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "11"
options.device_name = "Android Emulator"
options.app = "C:/Users/Yevhen/PycharmProjects/Automation/AppiumTests/app_wiki/wikipedia_2.7.50398.apk"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
mobile = Browser(Config(
    driver=driver,
    timeout=10))

"""
XPATH 
"//android.widget.ImageView[@name='Search Wikipedia']"
"""


def test_wiki():
    mobile.element(by.id('org.wikipedia:id/search_container')).click()
    # driver.find_element(By.ID, 'org.wikipedia:id/search_container').click()

    e = mobile.element(by.id("org.wikipedia:id/search_src_text"))
    # e = driver.find_element(By.ID, "org.wikipedia:id/search_src_text")
    e.clear()
    e.send_keys("Python")

    # text = driver.find_element(By.ID, 'org.wikipedia:id/page_list_item_title').text
    text = mobile.element(by.id('org.wikipedia:id/page_list_item_title')).get(query.text)

    assert 'Python' in text, f'Expected Python to be {text}'
