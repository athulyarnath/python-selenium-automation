from pages.base_page import BasePage
from pages.cart import Cart
from pages.header import Header
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.page = BasePage(driver)
        self.header = Header(self.page)
        self.main_page = MainPage(self.page)
        self.search_results = SearchResultPage(self.page)
        self.cart = Cart(self.page)
