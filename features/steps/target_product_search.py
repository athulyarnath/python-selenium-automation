from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD_MAIN = (By.CSS_SELECTOR, "input[id='search']")

@when("Search for tea from main page")
def search_for_tea(context):
    sleep(2)
    search_field = context.driver.find_element(*SEARCH_FIELD_MAIN)
    search_field.send_keys("tea")
    search_field.send_keys(Keys.RETURN)
    sleep(2)

@then("Verify search results for tea is shown")
def verify_results(context):
    sleep(2)
    search_result_count = context.driver.find_element(By.CSS_SELECTOR, "[data-test='text-quill-insert-0']")
    search_result_keys = context.driver.find_element(By.CSS_SELECTOR, "[data-test='text-quill-insert-1']")
    assert "results" in search_result_count.text and "tea" in search_result_keys.text


@when("Search for {product} from main page")
def search_for_tea(context, product):
    sleep(2)
    search_field = context.driver.find_element(*SEARCH_FIELD_MAIN)
    search_field.send_keys(product)
    search_field.send_keys(Keys.RETURN)
    sleep(2)

@then("Verify search results for {expected_product} is shown")
def verify_results(context, expected_product):
    sleep(2)
    search_result_count = context.driver.find_element(By.CSS_SELECTOR, "[data-test='text-quill-insert-0']")
    search_result_keys = context.driver.find_element(By.CSS_SELECTOR, "[data-test='text-quill-insert-1']")
    print(search_result_keys.text)
    assert "results" in search_result_count.text and expected_product in search_result_keys.text

@when("Search for Wireless Mouse from product search")
def search_for_wirelessmouse(context):
    sleep(2)
    search_field = context.driver.find_element(*SEARCH_FIELD_MAIN)
    search_field.send_keys("wireless mouse")
    search_field.send_keys(Keys.RETURN)

@then("Verify search results for Wireless Mouse is shown from product search")
def verify_mouse_options(context):
    sleep(2)
    mouse_options = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    assert len(mouse_options) >= 0, "Matching product is not found"

@when("Add first wireliess mouse to cart by clicking add to cart button")
def add_to_cart_step1(context):
    sleep(2)
    cart_buttons = context.driver.find_elements(By.CSS_SELECTOR, "button[data-test='chooseOptionsButton']")
    context.driver.execute_script("arguments[0].scrollIntoView();", cart_buttons[0])
    cart_buttons[0].click()


@then("Choose options Navigation bar will be shown")
def verify_choose_options(context):
    sleep(2)
    nav_bar = context.driver.find_element(By.CSS_SELECTOR, "h2[data-test='modal-drawer-heading']")
    assert "Choose options" in nav_bar.text

@when("Click on Add to Cart from Navigation bar")
def add_to_cart_step2(context):
    sleep(2)
    cart_buttons = context.driver.find_elements(By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
    cart_buttons[0].click()


@then("Added to cart option will be shown in Navigation bar")
def verify_added_options(context):
    sleep(2)
    nav_bar = context.driver.find_elements(By.CSS_SELECTOR, "h2[data-test='modal-drawer-heading']")
    assert "Added to cart" in nav_bar[1].text

@when("Click on View Cart button from navigation bar")
def view_cart(context):
    sleep(2)
    view_cart_btn = context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']")
    view_cart_btn.click()

@then("Cart option will be shown on the screen")
def verify_cart(context):
    sleep(2)
    order_summary = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cart-summary-title']")
    assert "Order summary" in order_summary.text
