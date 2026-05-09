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

driver.get('https://www.target.com/')

# Locate : Hiding the popup, By XPATH
popup_close_btn = driver.find_element(By.XPATH, '//button[@aria-label="close"]')
popup_close_btn.click()

# Locate : Click Account button, By XPATH
account_btn = driver.find_element(By.XPATH, '//a[@id="account-sign-in"]')
account_btn.click()

sleep(2)
# Locate : Click SignIn btn from side navigation, By XPATH
create_account_btn = driver.find_element(By.XPATH, '//button[@data-test="accountNav-signIn"]')
create_account_btn.click()

sleep(2)

# Locate : “Sign in or create account” text is shown, By XPATH
signin_txt = driver.find_element(By.XPATH, '//h1[contains(@class,"styles_ndsHeading")]')

if signin_txt.text == "Sign in or create account":
    print("Value : " + signin_txt.text)
    assert True
else:
    assert False

try:
    # Locate : “Sign in Button” , By XPATH
    sign_btn = driver.find_element(By.XPATH, '//*[@id="login"]')
    print("Located Button : " + sign_btn.text)
except NoSuchElementException:
    print("Continue Button not found")
    assert False

sleep(5)
driver.quit()