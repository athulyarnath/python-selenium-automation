from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.maximize_window()


driver.get('https://stackoverflow.com/users/signup')

sleep(10)

page_heading = driver.find_element(By.CSS_SELECTOR, "h1[class*='fs-headline1']")
by_clicking = driver.find_element(By.CSS_SELECTOR, "div[class*='fs-caption']")
email = driver.find_element(By.CSS_SELECTOR, "[id='email']")
password = driver.find_element(By.CSS_SELECTOR, "[id='password']")
show_password = driver.find_element(By.CSS_SELECTOR, "svg[class*='s-show-password']")
signup = driver.find_element(By.CSS_SELECTOR, "[id='submit-button']")
signup_google = driver.find_element(By.CSS_SELECTOR, "[data-provider='google']")
signup_github = driver.find_element(By.CSS_SELECTOR, "[data-provider='github']")

print(page_heading.text)

sleep(2)
driver.quit()