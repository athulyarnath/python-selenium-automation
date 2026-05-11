from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Home page in browser')
def open_target_home_page(context):
    context.driver.get('https://www.target.com/')

@when("Sign in for the best experience popup is open")
def best_experience_popup(context):
    sleep(2)
    popup = context.driver.find_element(By.CSS_SELECTOR, "[aria-live='assertive']")
    if popup is not None:
        assert "Popup window is visible"

@then("Close the popup")
def close_popup_window(context):
    sleep(2)
    popup_close_button = context.driver.find_element(By.CSS_SELECTOR, "[aria-label='close']")
    if popup_close_button.text is not None:
        popup_close_button.click()

