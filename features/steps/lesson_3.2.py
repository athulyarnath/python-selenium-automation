from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Home page')
def target_home_page(context):
    context.driver.get('https://www.target.com/')


@when("Click on Cart Icon")
def click_cart_icon(context):
    sleep(2)
    popup_close_button = context.driver.find_element(By.CSS_SELECTOR, ".styles_ndsButtonClose__GCWpq.styles_xs__iOov6.styles_closeButton___FCu0")
    if popup_close_button.text is not None:
        popup_close_button.click()

    cart_icon = context.driver.find_element(By.CSS_SELECTOR, ".styles_ndsLink__GUaai.styles_onLight__QKcK7.styles_neverDecorate__heNCW.styles_primaryHeaderLink__5Q2kU.styles_cartLink__DEGWh")
    cart_icon.click()
    sleep(7)


@then("Verify 'Your cart is empty' is displayed")
def verify_message(context):
    status_label = context.driver.find_element(By.CSS_SELECTOR, ".styles_ndsHeading__phw6r.styles_fontSize1__OL7f3.styles_x2Margin__ZKMpf")
    if status_label.text == "Your cart is empty":
        print("Yes, Your cart is empty")
        sleep(5)
    else:
        assert "No, Your cart is NOT empty"

@when("Click Sign In")
def click_sign_in(context):
    sleep(2)
    popup_close_button = context.driver.find_element(By.CSS_SELECTOR, ".styles_ndsButtonClose__GCWpq.styles_xs__iOov6.styles_closeButton___FCu0")
    if popup_close_button.text is not None:
        popup_close_button.click()

    sign_in_button = context.driver.find_element(By.CSS_SELECTOR, ".sc-40e81479-3.chaKyG.display-name.h-margin-r-x3")
    sign_in_button.click()
    sleep(2)

@then("Verify navigation menu opened on right side")
def verify_navigation_menu(context):
    sleep(2)
    navigation_menu = context.driver.find_element(By.CSS_SELECTOR, ".styles_ndsHeading__phw6r.styles_fontSize2__rqnzp.styles_x2Margin__ZKMpf.styles_heading__lrDgr")
    if navigation_menu.text is None:
        assert "Naviagtion Menu not opened"

@when("Click Sign In from Navigation menu")
def click_sign_in_button(context):
    sign_in_button = context.driver.find_element(By.CSS_SELECTOR, ".styles_btn__1hjpW.styles_base__3f8L_.styles_md__Jpg6t.styles_ndsButton__XOOOH.styles_md__Yc3tr.styles_filled___MOAP.styles_fullWidth__8m0Wc.h-margin-t-x2.h-margin-b-default")
    sign_in_button.click()

@then("Verify Sign In form opened")
def verify_sign_in_form_opened(context):
    continue_button = context.driver.find_element(By.CSS_SELECTOR, ".styles_btn__1hjpW.styles_base__3f8L_.styles_lg__hMlpX.styles_ndsButton__XOOOH.styles_lg__T5sAi.h-margin-t-x4")
    if continue_button.text is not None:
        print("Yes, Your are in Sign in form")
        sleep(5)
    else:
        assert "No, Unable to open sign in form"