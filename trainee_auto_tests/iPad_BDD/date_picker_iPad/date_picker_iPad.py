from pytest_bdd import scenario, when, then, given
import pytest

# @pytest.mark.which_app("ios_uicatalog")
@given('open_UICatalog')
def open_app(mobile):
    mobile.uicatalog_should_be_opened()


@when('user opens the date picker')
def open_date_picker(mobile):
    mobile.open_date_picker_iPad()


@then('date picker is opened')
def date_picker_should_be_opened(mobile):
    pass


@when('user opens the calendar')
def open_calendar(mobile):
    pass