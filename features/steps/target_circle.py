from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

TARGET_CIRCLE_LINK = (By.CSS_SELECTOR, "a[id='utilityNav-circle']")

@when("Click on Target Circle menu from main page")
def open_target_circle(context):
    sleep(2)
    target_circle_link = context.driver.find_element(*TARGET_CIRCLE_LINK)
    target_circle_link.click()
    sleep(2)


@then("2 story cards are shown under 'Unlock added value'")
def verify_storycards(context):
    sleep(2)
    story_cards = context.driver.find_elements(By.CSS_SELECTOR, "div[data-test='storycardWrapperElement-div']")
    assert len(story_cards) == 2, "Not found 2 story cards"
    for story_card in story_cards:
        print("Hello" + story_card.text)
    print(story_cards)


