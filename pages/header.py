from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Header(BasePage):

    SEARCH_FIELD_MAIN = (By.CSS_SELECTOR, "input[id='search']")

    def search_for_coffe(self):
        self.set_text_go(*self.SEARCH_FIELD_MAIN, text= "coffee")

    def click_cart_icon(self):
        popup_close_button = self.find_element(By.CSS_SELECTOR, "[aria-label='close']")
        if popup_close_button.text is not None:
            popup_close_button.click()

        self.click(By.CSS_SELECTOR, "[aria-label='cart 0 items']")
