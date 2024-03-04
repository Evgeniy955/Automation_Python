from time import sleep
import pytest
from appium import webdriver
from selene.support.shared import browser
from appium.options.ios import XCUITestOptions
from appium import webdriver as appium_driver
from selenium import webdriver
from selene import Browser, Config


options_iphone = XCUITestOptions()
options_iphone.platformName = 'iOS'
options_iphone.platformVersion = "17.2"
options_iphone.deviceName = "iPad Pro (12.9-inch) (6th generation)"
options_iphone.app = "com.3D4Medical.CAPhone"
options_iphone.newCommandTimeout = 2000
options_iphone.noReset = True
options_iphone.udid = "00F8A143-C723-42BB-8FDE-06DE20E89CC8"
options_iphone.autoAcceptAlerts = True
options_iphone.autoWebview = True
options_iphone.appPushTimeout = 300000
options_iphone.browserName = ''
options_iphone.includeSafariInWebviews = True
# options_iphone.automationName = 'XCUITest'
# options_iphone.platform = "IPHONE"


# appium_driver.Remote(
#             command_executor=driver_config.APPIUM_SERVER if RUN_LOCAL else driver_config.APPIUM_SERVER(),
#             options=options_iphone,
#         )




# browser_instance = Browser(Config(
#     driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options_iphone),
#     timeout=20,
# ))
# browser.config.driver = browser_instance.driver
appium_driver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub', options=options_iphone
)
sleep(20)
