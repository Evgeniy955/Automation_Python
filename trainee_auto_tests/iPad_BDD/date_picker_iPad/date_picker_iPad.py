from time import sleep

from pytest_bdd import scenario, when, then, given
import pytest


@pytest.mark.usefixtures("browser_catalog")
@given('open_UICatalog')
def open_app(browser_catalog):
    browser_catalog.uicatalog_should_be_opened()
    sleep(10)


@when('user opens the date picker')
def open_date_picker(browser_catalog):
    browser_catalog.open_date_picker_iPad()


@then('date picker is opened')
def date_picker_should_be_opened(browser_catalog):
    pass


@when('user opens the calendar')
def open_calendar(browser_catalog):
    pass