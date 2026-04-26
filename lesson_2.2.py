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
popup_close_btn = driver.find_element(By.XPATH, '//*[@id="headerPrimary"]/div[6]/button')
popup_close_btn.click()

# Locate : Click Account button, By XPATH
account_btn = driver.find_element(By.XPATH, '//*[@id="account-sign-in"]/span')
account_btn.click()

sleep(2)
# Locate : Click SignIn btn from side navigation, By XPATH
account_btn = driver.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/ul/div/button')
account_btn.click()

sleep(2)

# Locate : “Sign in or create account” text is shown, By XPATH
signin_txt = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[2]/div/div[1]/h1')

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

sleep(10)
driver.quit()