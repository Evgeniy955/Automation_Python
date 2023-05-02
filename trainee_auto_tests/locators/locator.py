from selene import by
from appium.webdriver.common.mobileby import MobileBy

#Test_1
catalog_menu_framework = (by.xpath('//android.view.View[@content-desc="Framework7 Material 1.4.0"]'))
catalog_calendar = (by.xpath("//*[@content-desc='Calendar / Datepicker ']"))
calendar_enabled = (by.xpath('//android.view.View[@content-desc="Calendar"]')) # .is_enabled()
open_calendar = (by.xpath('//*[@text="Select date range"]'))
date_from = (by.xpath('(//*[@content-desc="1"])[1]'))
date_to = (by.xpath('(//*[@content-desc="2"])[1]'))
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



