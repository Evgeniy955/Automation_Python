from time import sleep

import pytest


@pytest.mark.which_app("uicatalog")
def test_date_picker(mobile):
    mobile.tap_on_menu_framework()
    mobile.tap_on_catalog_calendar()
    mobile.is_enabled_calendar()
    mobile.date_picker_scroll()
    mobile.tap_on_open_calendar()
    sleep(2)
    mobile.tap_on_date_from()
    mobile.tap_on_date_to()
    mobile.tap_on_confirm_date()
    mobile.assert_value_date('May 30 2023 - May 31 2023')


@pytest.mark.which_app("check_prompt")
def test_show_prompt(mobile):
    mobile.tap_on_catalog_menu_photon()
    mobile.tap_on_dialogs()
    mobile.tap_on_show_promt()
    mobile.assert_header_popup_hello()
    mobile.assert_text_popup_hello()
    mobile.clear_field_popup()
    mobile.value_insert()
    mobile.tap_on_close_popup_hello()
    mobile.assert_header_popup_ins_value()
    mobile.assert_text_popup_ins_value()
    mobile.tap_on_close_popup_ins_value()


@pytest.mark.which_app("buyiphone")
def test_buy_iphone(mobile):
    mobile.url_address()
    mobile.click_iphone13pro()
    mobile.click_buy_button()
    mobile.click_iphone13pro_max()
    mobile.click_color()
    mobile.click_memory_device()
    mobile.click_connect_later()
    mobile.click_no_smartphone_to_trade()
    mobile.click_payment_option()
    mobile.click_one_time_payment()
    mobile.click_add_to_bag()
    mobile.assert_bag()
