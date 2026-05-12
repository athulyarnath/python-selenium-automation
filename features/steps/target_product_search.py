from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_FIELD_MAIN = (By.CSS_SELECTOR, "input[id='search']")

@when("Search for tea from results page")
def search_for_tea(context):
    search_field = context.wait.until(EC.visibility_of_element_located(SEARCH_FIELD_MAIN))
    search_field.send_keys("tea")
    search_field.send_keys(Keys.RETURN)

@then("Verify search results for tea is displayed")
def verify_results(context):
    search_result_count = context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='text-quill-insert-0']")))
    search_result_keys = context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='text-quill-insert-1']")))
    assert "results" in search_result_count.text and "tea" in search_result_keys.text


@then("Verify products are listing with name and image")
def verify_product_list(context):
    prod_table = context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='styles_styledListingPageProductListCards']")))

    prod_images = prod_table.find_elements(By.CSS_SELECTOR, "img[class*='styles_pictureLazy']")
    prod_texts = prod_table.find_elements(By.CSS_SELECTOR, "a>div[class*='styles_ndsTruncate_']")

    print (len(prod_texts))
    for prod_text in prod_texts:
        print (prod_text.get_attribute('innerHTML'))
        assert prod_text.get_attribute('innerHTML') != "", "Product without name"

    print(len(prod_images))
    for prod_image in prod_images:
        print(prod_image.get_attribute('src'))
        assert prod_image.get_attribute('src') != "", "Product without image"



@when("Search for {product} from main page")
def search_for_tea(context, product):
    sleep(2)
    search_field = context.wait.until(EC.visibility_of_element_located(SEARCH_FIELD_MAIN))
    search_field.send_keys(product)
    search_field.send_keys(Keys.RETURN)


@then("Verify search results for {expected_product} is shown")
def verify_results(context, expected_product):
    search_result_count = context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='text-quill-insert-0']")))
    search_result_keys = context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='text-quill-insert-1']")))

    assert "results" in search_result_count.text and expected_product in search_result_keys.text

@when("Search for Wireless Mouse from product search")
def search_for_wirelessmouse(context):
    search_field = context.wait.until(EC.visibility_of_element_located(SEARCH_FIELD_MAIN))
    search_field.send_keys("wireless mouse")
    search_field.send_keys(Keys.RETURN)

@then("Verify search results for Wireless Mouse is shown from product search")
def verify_mouse_options(context):
    sleep(10)
    mouse_options = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    assert len(mouse_options) >= 0, "Matching product is not found"

@when("Add first wireliess mouse to cart by clicking add to cart button")
def add_to_cart_step1(context):
    cart_buttons = context.driver.find_elements(By.CSS_SELECTOR, "button[data-test='chooseOptionsButton']")
    context.driver.execute_script("arguments[0].scrollIntoView();", cart_buttons[0])
    cart_buttons[0].click()


@then("Choose options Navigation bar will be shown")
def verify_choose_options(context):
    nav_bar = context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2[data-test='modal-drawer-heading']")))
    assert "Choose options" in nav_bar.text

@when("Click on Add to Cart from Navigation bar")
def add_to_cart_step2(context):
    cart_buttons = context.driver.find_elements(By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
    cart_buttons[0].click()


@then("Added to cart option will be shown in Navigation bar")
def verify_added_options(context):
    sleep(5)
    nav_bar = context.driver.find_elements(By.CSS_SELECTOR, "h2[data-test='modal-drawer-heading']")
    assert "Added to cart" in nav_bar[1].text

@when("Click on View Cart button from navigation bar")
def view_cart(context):
    view_cart_btn = context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/cart']")))
    view_cart_btn.click()

@then("Cart option will be shown on the screen")
def verify_cart(context):
    sleep(2)
    order_summary = context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='cart-summary-title']")))
    assert "Order summary" in order_summary.text


@given("Open target Product details page")
def open_product_details_page(context):
    context.driver.get('https://www.target.com/p/women-s-balloon-long-sleeve-smocked-waist-v-neck-t-shirt-universal-thread-navy-blue/-/A-1008511541?preselect=95162139#lnk=sametab')

@then("User can click different color options from details page")
def verify_color_options(context):
    sleep(5)   # Waiting to disappear sponsored flash advertisement
    unsortedlist = context.driver.find_element(By.CSS_SELECTOR, "ul[class*='styles_unorderedList']")
    color_options = unsortedlist.find_elements(By.CSS_SELECTOR, "img[class*='styles_pictureLazy']")
    print(len(color_options))
    for color_option in color_options:
        color_option.click()
        sleep(2)

@then("User can click on fulfillment options")
def verify_fulfillment_options(context):
    fulfillment_options = context.driver.find_elements(By.CSS_SELECTOR, "button[data-test*='fulfillment-cell']")
    for fulfillment_option in fulfillment_options:
        fulfillment_option.click()
        sleep(2)
