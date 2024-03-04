from appium.options.android import UiAutomator2Options
from appium.options.ios import SafariOptions
from selenium import webdriver
from appium.options.ios import XCUITestOptions
import pytest
from appium import webdriver
from selene.support.shared import browser

# from functions_ipad.buy_iphone import Byiphone
from selene import Browser, Config


options_catalog = UiAutomator2Options()
options_catalog.platform_name = "Android"
options_catalog.platform_version = "13"
# options_catalog.device_name = "Android Emulator"
options_catalog.device_name = "db454744"
options_catalog.app_package = "org.eniblo.uicatalog"
options_catalog.app_activity = "org.eniblo.uicatalog.MainActivity"
# options_catalog.app = "/Users/halitsy.y/PycharmProjects/UIcatalog/trainee_auto_tests/app_UICatalog/UI Framework Catalog_v0.3.0.apk"


# cap, instance = config[which_app]
browser_instance = Browser(Config(
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options_catalog),
    timeout=20,
))
browser.config.driver = browser_instance.driver

browser_instance.quit()