from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Home page')
def target_home_page(context):
    context.driver.get('https://www.target.com/')


@when("Click on Cart Icon")
def click_cart_icon(context):
    sleep(2)
    popup_close_button = context.driver.find_element(By.CSS_SELECTOR, "[aria-label='close']")
    if popup_close_button.text is not None:
        popup_close_button.click()

    cart_icon = context.driver.find_element(By.CSS_SELECTOR, "[aria-label='cart 0 items']")
    cart_icon.click()
    sleep(7)


@then("Verify 'Your cart is empty' is displayed")
def verify_message(context):
    status_label = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")
    if status_label.text == "Your cart is empty":
        print("Yes, Your cart is empty")
        sleep(5)
    else:
        assert "No, Your cart is NOT empty"

@when("Click Sign In")
def click_sign_in(context):
    sleep(2)
    popup_close_button = context.driver.find_element(By.CSS_SELECTOR, "[aria-label='close']")
    if popup_close_button.text is not None:
        popup_close_button.click()

    sign_in_button = context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Account, sign in']")
    sign_in_button.click()
    sleep(2)

@then("Verify navigation menu opened on right side")
def verify_navigation_menu(context):
    sleep(2)
    navigation_menu = context.driver.find_element(By.CSS_SELECTOR, "[data-test='modal-drawer-heading']")
    if navigation_menu.text is None:
        assert "Navigation Menu not opened"

@when("Click Sign In from Navigation menu")
def click_sign_in_button(context):
    sign_in_button = context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    sign_in_button.click()

@then("Verify Sign In form opened")
def verify_sign_in_form_opened(context):
    continue_button = context.driver.find_element(By.CSS_SELECTOR, "[id='login']")
    if continue_button.text is not None:
        print("Yes, Your are in Sign in form")
        sleep(5)
    else:
        assert "No, Unable to open sign in form"