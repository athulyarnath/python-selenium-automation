from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

POPUP_WINDOW = (By.CSS_SELECTOR, "[aria-live='assertive']")
POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, "[aria-label='close']")

@given('Open Target Home page in browser')
def open_target_home_page(context):
    context.driver.get('https://www.target.com/')

@when("Sign in for the best experience popup is open")
def best_experience_popup(context):
    popup = context.driver.find_element(*POPUP_WINDOW)
    if popup is not None:
        assert "Popup window is visible"

@then("Close the popup")
def close_popup_window(context):
    popup_close_button = context.driver.find_element(*POPUP_CLOSE_BUTTON)
    if popup_close_button.text is not None:
        popup_close_button.click()

