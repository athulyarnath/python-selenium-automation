from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/help')
sleep(1)


page_header = driver.find_element(By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")
print(page_header.text)

have_question = driver.find_elements(By.CSS_SELECTOR, "h2[class*='styles_ndsHeading']")[0]
print(have_question.text)

browse_help = driver.find_element(By.CSS_SELECTOR, "button[class*='FlyoutKnowledge_noWhiteOutline']")
print(browse_help.text)

search_help_topic = driver.find_element(By.CSS_SELECTOR, "input[name='ArticleSearch']")
print(search_help_topic.text)

what_you_header = driver.find_elements(By.CSS_SELECTOR, "h2[class*='styles_ndsHeading']")[1]
print(what_you_header.text)

what_you_header_options = driver.find_elements(By.CSS_SELECTOR, "a[class*='styles_ndsLink']")
print(len(what_you_header_options))
assert len(what_you_header_options) >= 1, "Header options not found"

popular_pages_header = driver.find_elements(By.CSS_SELECTOR, "h2[class*='styles_ndsHeading']")[2]
print(popular_pages_header.text)

popular_pages = driver.find_elements(By.CSS_SELECTOR, "div[data-test='LinkList']")
print(len(popular_pages))
assert len(popular_pages) >= 1, "Popular Pages Not Found"


