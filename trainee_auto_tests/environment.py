from appium.options.android import UiAutomator2Options
from appium.options.ios import SafariOptions
from selenium import webdriver
from appium.options.ios import XCUITestOptions


options_catalog = UiAutomator2Options()
options_catalog.platform_name = "Android"
options_catalog.platform_version = "13"
# options_catalog.device_name = "Android Emulator"
options_catalog.device_name = "9A191FFAZ004MA"
options_catalog.app_package = "org.eniblo.uicatalog"
options_catalog.app_activity = "org.eniblo.uicatalog.MainActivity"
options_catalog.app = "/Users/halitsy.y/PycharmProjects/Automation_Python/trainee_auto_tests/app_UICatalog/UI Framework Catalog_v0.3.0.apk"


chrome_options = webdriver.ChromeOptions()
chrome_options.platform_name = 'Android'
chrome_options.platform_version = '13'
chrome_options.device_name = '9A191FFAZ004MA'
chrome_options.app_package = 'com.android.chrome'
# chrome_options.base_url = 'https://www.apple.com/iphone/buy'


DESIRED_CAPS_IOS = XCUITestOptions()
DESIRED_CAPS_IOS.app = "/Users/halitsy.y/Desktop/xcode_project/uicatalog/UICatalogIPA/Apps/UICatalog.ipa"
DESIRED_CAPS_IOS.device_name = "iPhone X"
DESIRED_CAPS_IOS.no_reset = False
DESIRED_CAPS_IOS.udid = "af72c51c9bc0c4b17d3f0fcfbe353689c5bd64c1"


DESIRED_CAPS_IOS_2 = {
  "deviceName": "iPhone X",
  "platformName": "iOS",
  "platformVersion": "15.4.1",
  "app": "/Users/halitsy.y/Desktop/xcode_project/uicatalog/UICatalogIPA/Apps/UICatalog.ipa",
  "noReset": True,
  "automationName": "XCUITest",
  "udid": "af72c51c9bc0c4b17d3f0fcfbe353689c5bd64c1"
}