Feature: Tests for Wiki Search

  Scenario: User can search and correct result is shown
    Given Tap on Search field
    When Enter Python to search field
    Then Result for Python is shown
