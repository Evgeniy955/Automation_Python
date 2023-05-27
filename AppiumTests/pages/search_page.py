from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchPage(Page):
    SEARCH_FIELD = (By.ID, "org.wikipedia:id/search_src_text")
    SEARCH_RESULT = (By.ID, 'org.wikipedia:id/page_list_item_title')

    def input_search(self, search_phrase: str):
        self.input(search_phrase, *self.SEARCH_FIELD)

    def verify_search_result(self, search_phrase: str):
        result_text = self.find_element(*self.SEARCH_RESULT).text
        assert search_phrase in result_text, f'Expected {search_phrase} to be {result_text}'