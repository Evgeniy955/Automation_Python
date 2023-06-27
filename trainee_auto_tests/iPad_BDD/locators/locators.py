from selene import by

from trainee_auto_tests.functions.func import time_now

# from functions.func import time_now

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
            'IOS' : '//XCUIElementTypeButton[@name="Thursday, 22 June"]/XCUIElementTypeOther[2]'}.get(ENV)
date_to = {'ANDROID' : by.xpath('(//android.view.View[@content-desc="2"])[1]')}.get(ENV)
time = {'IOS' : f'//XCUIElementTypeButton[@name="{time_now[0]}"] | //XCUIElementTypeButton[@name="{time_now[1]}"] | '
                f'//XCUIElementTypeButton[@name="{time_now[2]}"]'}.get(ENV)
# time_new = {'IOS' : f'//XCUIElementTypeButton[@name="{time_now()[1]}"]'}.get(ENV)
# time_new_1 = {'IOS' : f'//XCUIElementTypeButton[@name="{time_now()[2]}"]'}.get(ENV)
time_picker_popup = {'IOS' : '//XCUIElementTypePickerWheel[1]'}.get(ENV)
# time_picker_popup = {'IOS' : '//*[contains(@value, "17 o’clock"]'}.get(ENV)
# close_date_popup = {'IOS' : '//XCUIElementTypeStaticText[@name="Date Picker"]'}.get(ENV)
confirm_date = (by.xpath('//*[@content-desc="DONE"]'))
view_date = (by.xpath('//*[@resource-id="ks-calendar-range"]'))

# Test_2




