from selene import by

from functions.func import time_now

# QA_URL = {'DEV': 'https://d-openapi-test.zysbox.dev',
# #           'QA': 'https://q-openapi-test.zysbox.dev'}.get(ENV)
ENV = 'IOS'

#Test_1
catalog_menu_framework = (by.xpath('//android.view.View[@content-desc="Framework7 Material 1.4.0"]'))
catalog_calendar = {'ANDROID' : by.xpath("//*[@content-desc='Calendar / Datepicker ']"),
                    'IOS' : '//XCUIElementTypeStaticText[@name="Date Picker"]'}.get(ENV)


calendar_enabled = (by.xpath('//android.view.View[@content-desc="Calendar"]')) # .is_enabled()
# open_calendar = (by.xpath('//*[@text="Select date range"]'))
open_calendar = {'ANDROID' : by.xpath('//*[@resource-id="ks-calendar-range"]'),
                'IOS' : '//XCUIElementTypeOther[@name="Date and Time Picker"]'}.get(ENV)
date_from = {'ANDROID' : by.xpath('(//android.view.View[@content-desc="1"])[1]'),
            'IOS' : '//XCUIElementTypeButton[@name="Thursday, 15 June"]/XCUIElementTypeOther[2]'}.get(ENV)
date_to = {'ANDROID' : by.xpath('(//android.view.View[@content-desc="2"])[1]')}.get(ENV)
time = {'IOS' : f'//XCUIElementTypeButton[@name="{time_now()[0]}"]'}.get(ENV)
time_new = {'IOS' : f'//XCUIElementTypeButton[@name="{time_now()[1]}"]'}.get(ENV)
time_new_1 = {'IOS' : f'//XCUIElementTypeButton[@name="{time_now()[2]}"]'}.get(ENV)
time_picker_popup = {'IOS' : '//XCUIElementTypePickerWheel[1]'}.get(ENV)
# time_picker_popup = {'IOS' : '//*[contains(@value, "17 o’clock"]'}.get(ENV)
# close_date_popup = {'IOS' : '//XCUIElementTypeStaticText[@name="Date Picker"]'}.get(ENV)
confirm_date = (by.xpath('//*[@content-desc="DONE"]'))
view_date = (by.xpath('//*[@resource-id="ks-calendar-range"]'))

# Test_2
catalog_menu_photon = (by.xpath('//*[@content-desc="Phonon 1.3.1"]'))
dialogs = (by.xpath('//*[@content-desc="Dialogs"]'))
show_promt = (by.xpath('//android.widget.Button[@content-desc="SHOW PROMPT"]'))
popup_hello = (by.xpath('//*[@content-desc="Hello"]'))
text_example = (by.xpath('//*[@content-desc="Example"]'))
field_value = (by.xpath('//*[contains(@text,"Value")]'))
close_popup = (by.xpath('//*[@content-desc="OK"]'))
inserted_value_popup = (by.xpath('//*[@content-desc="Inserted Value"]'))
value_popup = (by.xpath('//*[@content-desc="Test"]'))

# Test_3
iphone13pro = (by.xpath("//*[@class='chapternav-item chapternav-item-iphone-13-pro']"))
buy_button = (by.xpath('//*[@class="ac-ln-action ac-ln-action-button"]'))
iphone13pro_max  = (by.xpath("//*[@value='6_7inch']"))
color = (by.xpath("//*[@value='silver']"))
memory_device = (by.xpath("//*[@value='512gb']"))
connect_later = (by.xpath("//*[@value='UNLOCKED/US']"))
no_smartphone_to_trade = (by.xpath("//*[@value='noTradeIn']"))
payment_option = (by.xpath("//*[@value='fullPrice']"))
one_time_payment = (by.xpath("//*[@value='add-to-cart']"))
add_to_bag = (by.xpath("//*[@class='button button-block']"))
review_bag = (by.xpath("//*[@class='rs-iteminfo-title']"))



