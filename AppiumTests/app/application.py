from pages.main_page import MainPage
from pages.search_page import SearchPage

class Application:

    def __init__(self,driver):
        self.main_page= MainPage(driver)
        self.search_page = SearchPage(driver)
