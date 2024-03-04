import subprocess
from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.options.ios import XCUITestOptions
from selene.support.shared import browser
from appium.webdriver.common.appiumby import AppiumBy
from selene import Browser, Config
from appium import webdriver as appium_driver

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

RUN_LOCAL = True
PLATFORM = "IPAD"

# if RUN_LOCAL:
#     _capabilities = {
#         "ANDROID_TABLET": {
#
#         },
#         "IPAD": {
#
#         },
#         "IPHONE": {
#
#         },
#     }


# Android_Tablet
options_android_phone = UiAutomator2Options()
options_android_phone.platform_name = "Android"
options_android_phone.platform_version = "13"
options_android_phone.device_name = "emulator-5554"
options_android_phone.app_package = "com.a3d4medical.completeanatomy"
options_android_phone.app_activity = "com.a3d4medical.completeanatomy.MainActivitySingle"

_caps = {
    "ANDROID_TABLET": {
        "platformName": "Android",
        "appium:orientation": "LANDSCAPE",
        "appium:platformVersion": "14",
        "appium:deviceName": "emulator-5554",
        "appium:new_command_timeout": 2000,
        "appium:auto_grant_permissions": True,
        "appium:appPackage": "com.a3d4medical.completeanatomy",
        "appium:appActivity": "com.a3d4medical.completeanatomy.MainActivitySingle",
# app_wait_activity
        # "appium:chromedriver_executable": set_chromedriver_executable(),
        "appium:automationName": "UiAutomator2",
        "appium:unicodeKeyboard": True,
        "appium:resetKeyboard": True,
        },
    "ANDROID_PHONE": {
        "platformName": "Android",
        "appium:orientation": "PORTRAIT",
        "appium:platformVersion": "13",
        "appium:deviceName": "db454744",
        "appium:new_command_timeout": 2000,
        "appium:auto_grant_permissions": True,
        "appium:appPackage": "com.a3d4medical.completeanatomy",
        "appium:appActivity": "com.a3d4medical.completeanatomy.MainActivitySingle",
        "appium:automationName": "UiAutomator2",
        "appium:unicodeKeyboard": True,
        "appium:resetKeyboard": True,
        },
    "IPHONE": {
        "platformName": 'iOS',
        "appium:platformVersion": "17.2",
        "appium:deviceName": "iPhone 15 Pro",
        "appium:app": "com.3D4Medical.CAPhone",
        "appium:new_command_timeout": 2000,
        "appium:no_reset": True,
        "appium:udid": "56542542-B7DF-4115-A640-555E78613AB3",
        "appium:auto_accept_alerts": True,
        "appium:auto_web_view": True,
        "appium:app_push_timeout": 300000,
        "browser_name": '',
        "appium:include_safari_in_webview": True,
        "appium:automation_name": 'XCUITest',
        },
    "IPAD": {
        # "platformName": "iOS",
        # "appium:platformVersion": "15.2",
        # "appium:deviceName": "iPad Pro (11-inch) (3rd generation)",
        # uncomment if you want to run test with full reset after each test on local device(app will be installed
        # # from .ipa file)
        # "app": "com.3D4Medical.CA" if RUN_ON_LOCAL_SIM else config.driver_config.MOBILE_APP,
        "appium:app": "com.3D4Medical.CA",
        "appium:new_command_timeout": 2000,
        "appium:no_reset": True,
        # 'xcodeOrgId': config.driver_config.X_CODE_TEAM_ID,
        # 'xcodeSigningId': 'iPhone Developer',
        # "appium:udid": "95519329-78AB-48B2-AE2D-27043F16BCE0",
        "appium:auto_accept_alerts": True,
        # 'wdaLocalPort': config.driver_config.WDA_PORT,
        # 'fullReset': True,
        # 'useNewWDA': True,
        # 'maxTypingFrequency': 30
        "appium:auto_web_view": True,
        "appium:app_push_timeout": 300000,
        "browser_name": "",
        "appium:include_safari_in_webview": True,
        "appium:automation_name": "XCUITest",
    },
}

# iPad
# options_ipad = XCUITestOptions()
# options_ipad.platform_name = 'iOS'
# options_ipad.platform_version = config.driver_config.IPAD_VERSION
# options_ipad.device_name = config.driver_config.IPAD_DEVICE_NAME
# # uncomment if you want to run test with full reset after each test on local device(app will be installed
# # from .ipa file)
# # "app": "com.3D4Medical.CA" if RUN_ON_LOCAL_SIM else config.driver_config.MOBILE_APP,
# options_ipad.app = "com.3D4Medical.CA"
# options_ipad.new_command_timeout = config.driver_config.APPIUM_TIMEOUT
# options_ipad.no_reset = True
# # 'xcodeOrgId': config.driver_config.X_CODE_TEAM_ID,
# # 'xcodeSigningId': 'iPhone Developer',
# options_ipad.udid = config.driver_config.IPAD_DEVICE_UDID
# options_ipad.auto_accept_alerts = True
# # 'wdaLocalPort': config.driver_config.WDA_PORT,
# # 'fullReset': True,
# # 'useNewWDA': True,
# # 'maxTypingFrequency': 30,
# options_ipad.auto_web_view = True
# options_ipad.app_push_timeout = 300000
# options_ipad.browser_name = ""
# options_ipad.include_safari_in_webview = True
# options_ipad.automation_name = 'XCUITest'

# New Apad
new_options = XCUITestOptions()
new_options.platformName = 'iOS'
new_options.set_capability("appium:platformVersion", "17.2")
new_options.set_capability("appium:deviceName", "iPad Pro (12.9-inch) (6th generation)")
new_options.set_capability("appium:app", "com.3D4Medical.CA")
new_options.set_capability("appium:new_command_timeout", 2000)
new_options.set_capability("appium:no_reset", True)
new_options.set_capability("appium:udid", "00F8A143-C723-42BB-8FDE-06DE20E89CC8")
new_options.set_capability("appium:auto_accept_alerts", True)
new_options.set_capability("appium:auto_web_view", True)
new_options.set_capability("appium:app_push_timeout", 300000)
# new_options.set_capability("appium:browser_name", "")
new_options.set_capability("browser_name", "")
new_options.set_capability("appium:include_safari_in_webview", True)
new_options.set_capability("appium:automationName", "XCUITest")

# appium_options = AppiumOptions()
# capabilities_ipad = appium_options.to_capabilities()
# iPad 2


options = XCUITestOptions() if PLATFORM in ["IPHONE", "IPAD"] else UiAutomator2Options()
options.load_capabilities(
    _caps.get(PLATFORM)
)

# iPhone
options_iphone = XCUITestOptions()
options_iphone.platform_name = "iOS"
options_iphone.platform_version = "17.2"
options_iphone.device_name = "iPhone 15"
options_iphone.app = "com.3D4Medical.CAPhone"
options_iphone.new_command_timeout = 2000
options_iphone.no_reset = True
options_iphone.udid = "52DC0FDB-C1E6-44CD-9CAB-57079CAC0249"
options_iphone.auto_accept_alerts = True
options_iphone.auto_web_view = True
options_iphone.app_push_timeout = 300000
options_iphone.browser_name = ''
options_iphone.include_safari_in_webview = True
options_iphone.automation_name = 'XCUITest'

# if RUN_LOCAL:
#     _capabilities = {
#         "ANDROID_TABLET": options,
#         "IPAD": appium_options,
#         "NEW_IPAD": new_options,
#         "IPHONE": options_iphone
#     }
# else:
#     _capabilities = {}
options.set_capability("platformName", "iOS")
options.set_capability("appium:platformVersion", "15.2")
options.set_capability("appium:deviceName", "iPad Pro (11-inch) (3rd generation)")
options.set_capability("appium:udid", "95519329-78AB-48B2-AE2D-27043F16BCE0")


options_device = options



subprocess.getoutput('adb devices')
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=caps)

browser_instance = appium_driver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", options=options_device)
# browser_instance = Browser(Config(
#     driver=webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', options=options),
#     timeout=20,
# ))
browser.config.driver = browser_instance

web_view = browser.driver.contexts[-1]
# browser.driver.capabilities
browser.driver.switch_to.context(browser.driver.contexts[-1])

sleep(20)
browser_instance.quit()
