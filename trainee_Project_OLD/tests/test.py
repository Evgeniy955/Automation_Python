import pytest



@pytest.mark.which_app("uicatalog")
def test_date_picker(driver):
    driver.tap_on_menu_framework()
    driver.tap_on_catalog_calendar()
    driver.is_enabled_calendar()
    driver.date_picker_scroll()
    driver.tap_on_open_calendar()
    driver.tap_on_date_from()
    driver.tap_on_date_to()
    driver.tap_on_confirm_date()
    driver.assert_value_date('Jul 29 2022 - Jul 30 2022')


@pytest.mark.which_app("check_prompt")
def test_show_prompt(driver):
    driver.tap_on_catalog_menu_photon()
    driver.tap_on_dialogs()
    driver.tap_on_show_promt()
    driver.assert_header_popup_hello()
    driver.assert_text_popup_hello()
    driver.clear_field_popup()
    driver.value_insert()
    driver.tap_on_close_popup_hello()
    driver.assert_header_popup_ins_value()
    driver.assert_text_popup_ins_value()
    driver.tap_on_close_popup_ins_value()


@pytest.mark.which_app("buyiphone")
def test_buy_iphone(driver):
    driver.url_address()
    driver.click_iphone13pro()
    driver.click_buy_button()
    driver.click_iphone13pro_max()
    driver.click_color()
    driver.click_memory_device()
    driver.click_connect_later()
    driver.click_no_smartphone_to_trade()
    driver.click_payment_option()
    driver.click_one_time_payment()
    driver.click_add_to_bag()
    driver.assert_bag()

