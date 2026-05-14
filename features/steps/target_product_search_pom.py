from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Target main page')
def open_target_main_page(context):
    context.app.main_page.go_to_main_page()

@when("Best experience sign in popup is open")
def best_experience_sign_in_popup(context):
    context.app.main_page.best_experience_sign_in_popup()

@then("Close best experience popup")
def close_best_experience_popup(context):
    context.app.main_page.close_popup_window()

@when("Search for coffe from header")
def search_for_coffe(context):
    context.app.header.search_for_coffe()

@then("Verify search results displays coffee")
def verify_search_results_displays_coffee(context):
    context.app.search_results.verify_search_results_displays_coffee()

@then("Verify coffees are showing with name and image")
def verify_results_displayed_with_name_image(context):
    context.app.search_results.verify_results_displayed_with_name_image()

@when("Click on Cart Icon from header")
def click_cart_icon(context):
    context.app.header.click_cart_icon()

@then("Verify 'Your cart is empty' is shown")
def verify_cart_is_empty(context):
    context.app.cart.verify_cart_is_empty()
