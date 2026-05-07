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

element = driver.find_element(By.CSS_SELECTOR, ".flex--item.fs-headline1")
by_clicking = driver.find_element(By.CSS_SELECTOR, ".flex--item.js-terms.fs-caption.fc-black-400.ta-left")
email = driver.find_element(By.CSS_SELECTOR, ".flex--item.s-label")
password = driver.find_element(By.CSS_SELECTOR, ".flex--item.s-label")
show_password = driver.find_element(By.CSS_SELECTOR, ".ps-absolute.r8.t8.c-pointer.js-hide-password.svg-icon.iconEyeSm")
signup = driver.find_element(By.CSS_SELECTOR, ".flex--item.s-btn.s-btn__filled")
signup_google = driver.find_element(By.CSS_SELECTOR, ".flex--item.s-btn.s-btn__icon.s-btn__google.bar-md.ba.bc-black-225")
signup_github = driver.find_element(By.CSS_SELECTOR, ".flex--item.s-btn.s-btn__icon.s-btn__github.bar-md.ba.bc-black-225")

print(element.text)

sleep(10)
driver.quit()