from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    POPUP_WINDOW = (By.CSS_SELECTOR, "[aria-live='assertive']")
    POPUP_CLOSE_BUTTON = ((By.CSS_SELECTOR, "[aria-label='close']"))

    MAIN_URL = "https://www.target.com/"

    def go_to_main_page(self):
        self.open(self.MAIN_URL)

    def best_experience_sign_in_popup(self):
        popup = self.find_element(*self.POPUP_WINDOW)
        if popup is not None:
            assert "Popup window is visible"

    def close_popup_window(self):
        popup = self.find_element(*self.POPUP_WINDOW)
        if popup is not None:
            self.click(*self.POPUP_CLOSE_BUTTON)
