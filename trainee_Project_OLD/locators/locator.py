from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy

#Test_1
catalog_menu_framework = (AppiumBy.ACCESSIBILITY_ID, "Framework7 Material 1.4.0")
catalog_calendar = (MobileBy.XPATH, "//*[@content-desc='Calendar / Datepicker ']")
calendar_enabled = (MobileBy.XPATH, '//android.view.View[@content-desc="Calendar"]') # .is_enabled()
open_calendar = (MobileBy.XPATH, '//*[@content-desc="Autocomplete "]')
date_from = (MobileBy.XPATH, '(//*[@content-desc="1"])[1]')
date_to = (MobileBy.XPATH, '(//*[@content-desc="2"])[1]')
confirm_date = (MobileBy.XPATH, '//*[@content-desc="DONE"]')
view_date = (MobileBy.XPATH, '//*[@resource-id="ks-calendar-range"]')

# Test_2
catalog_menu_photon = (MobileBy.XPATH, '//*[@content-desc="Phonon 1.3.1"]')
dialogs = (MobileBy.XPATH, '//*[@content-desc="Dialogs"]')
show_promt = (MobileBy.ACCESSIBILITY_ID, 'SHOW PROMPT')
popup_hello = (MobileBy.XPATH, '//*[@content-desc="Hello"]')
text_example = (MobileBy.XPATH, '//*[@content-desc="Example"]')
field_value = (MobileBy.XPATH, '//*[contains(@text,"Value")]')
close_popup = (MobileBy.XPATH, '//*[@content-desc="OK"]')
inserted_value_popup = (MobileBy.XPATH, '//*[@content-desc="Inserted Value"]')
value_popup = (MobileBy.XPATH, '//*[@content-desc="Test"]')

# Test_3
iphone13pro = (MobileBy.XPATH, "//*[@class='chapternav-item chapternav-item-iphone-13-pro']")
buy_button = (MobileBy.XPATH, '//*[@class="ac-ln-action ac-ln-action-button"]')
iphone13pro_max  = (MobileBy.XPATH, "//*[@value='6_7inch']")
color = (MobileBy.XPATH, "//*[@value='silver']")
memory_device = (MobileBy.XPATH, "//*[@value='512gb']")
connect_later = (MobileBy.XPATH, "//*[@value='UNLOCKED/US']")
no_smartphone_to_trade = (MobileBy.XPATH, "//*[@value='noTradeIn']")
payment_option = (MobileBy.XPATH, "//*[@value='fullPrice']")
one_time_payment = (MobileBy.XPATH, "//*[@value='add-to-cart']")
add_to_bag = (MobileBy.XPATH, "//*[@class='button button-block']")
review_bag = (MobileBy.XPATH, "//*[@class='rs-iteminfo-title']")



