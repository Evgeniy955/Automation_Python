from selenium.webdriver.common.by import By

from pages.base_page import Page

class MainPage(Page):
    SEARCH = (By.ID, 'org.wikipedia:id/search_container')

    def tap_search(self):
        self.click(*self.SEARCH)
