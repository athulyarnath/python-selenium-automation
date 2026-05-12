from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

TARGET_CIRCLE_LINK = (By.CSS_SELECTOR, "a[id='utilityNav-circle']")

@when("Click on Target Circle menu from main page")
def open_target_circle(context):
    target_circle_link = context.wait.until(EC.visibility_of_element_located(TARGET_CIRCLE_LINK))
    target_circle_link.click()


@then("2 story cards are shown under 'Unlock added value'")
def verify_storycards(context):
    story_cards = context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-test='storycardWrapperElement-div']")))
    assert len(story_cards) == 2, "Not found 2 story cards"
    for story_card in story_cards:
        print("Hello" + story_card.text)
    print(story_cards)


