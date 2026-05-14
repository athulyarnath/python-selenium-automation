from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class Cart(BasePage):
    def verify_cart_is_empty(self):
        status_label = self.find_element(By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")
        if status_label.text == "Your cart is empty":
            print("Yes, Your cart is empty")
        else:
            assert "No, Your cart is NOT empty"