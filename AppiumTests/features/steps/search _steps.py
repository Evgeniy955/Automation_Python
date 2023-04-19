from behave import given, when, then
'''
  Scenario: User can search and correct result is shown
    Given Tap on Search field
    When Enter Python to search field
    Then Result for Python is shown
'''
@given('Tap on Search field')
def tap_search(context):
    context.app.main_page.tap_search()

@when('Enter {search_phrase} to search field')
def input_search(context, search_phrase):
    context.app.search_page.input_search(search_phrase)

@then('Result for {search_phrase} is shown')
def verify_search_result(context, search_phrase):
    context.app.search_page.verify_search_result(search_phrase)
