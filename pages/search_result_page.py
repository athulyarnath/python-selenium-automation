from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultPage(BasePage):

    SEARCH_RESULT_COUNT = (By.CSS_SELECTOR, "[data-test='text-quill-insert-0']")
    SEARCH_RESULT_KEYS = (By.CSS_SELECTOR, "[data-test='text-quill-insert-1']")

    PRODUCT_TABLE = (By.CSS_SELECTOR, "[class*='styles_styledListingPageProductListCards']")

    PRODUCT_IMAGES = (By.CSS_SELECTOR, "img[class*='styles_pictureLazy']")
    PRODUCT_TEXTS = (By.CSS_SELECTOR, "a>div[class*='styles_ndsTruncate_']")

    def verify_search_results_displays_coffee(self):
        search_result_count = self.find_element(*self.SEARCH_RESULT_COUNT)
        search_result_keys = self.find_element(*self.SEARCH_RESULT_KEYS)
        assert "results" in search_result_count.text and "coffee" in search_result_keys.text

    def verify_results_displayed_with_name_image(self):
        prod_table = self.find_element(*self.PRODUCT_TABLE)

        prod_images = prod_table.find_elements(*self.PRODUCT_IMAGES)
        prod_texts = prod_table.find_elements(*self.PRODUCT_TEXTS)

        print(len(prod_texts))
        for prod_text in prod_texts:
            print(prod_text.get_attribute('innerHTML'))
            assert prod_text.get_attribute('innerHTML') != "", "Product without name"

        print(len(prod_images))
        for prod_image in prod_images:
            print(prod_image.get_attribute('src'))
            assert prod_image.get_attribute('src') != "", "Product without image"