from appium.options.android import UiAutomator2Options
from selenium import webdriver


options_catalog = UiAutomator2Options()
options_catalog.platform_name = "Android"
options_catalog.platform_version = "13"
# options_catalog.device_name = "Android Emulator"
options_catalog.device_name = "9A191FFAZ004MA"
options_catalog.app_package = "org.eniblo.uicatalog"
options_catalog.app_activity = "org.eniblo.uicatalog.MainActivity"
options_catalog.app = "C:/Users/Yevhen/PycharmProjects/Automation/trainee_auto_tests/app_UICatalog/UI Framework Catalog_v0.3.0.apk"


chrome_options = webdriver.ChromeOptions()
chrome_options.platform_name = 'Android'
chrome_options.platform_version = '13'
chrome_options.device_name = '9A191FFAZ004MA'
chrome_options.app_package = 'com.android.chrome'
# chrome_options.base_url = 'https://www.apple.com/iphone/buy'


