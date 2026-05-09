from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver_path = ChromeDriverManager().install()


service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#driver.get('https://www.amazon.com/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F%26tag%3Damazusnavi-20%26ref%3Dnav_ya_signin%26adgrpid%3D185319704606%26hvpone%3D%26hvptwo%3D%26hvadid%3D793056977215%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D10508722049456496289%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9019615%26hvtargid%3Dkwd-360364908397%26hydadcr%3D28884_15009378_1546077%26mcid%3Dadfdaf019ea13ff5af2dd6b5b801add6%26hvocijid%3D10508722049456496289--%26hvexpln%3D0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fyour-orders%2Forders%3Fref_%3Dya_d_c_yo&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_retail_yourorders_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Locate : Amazon logo, By XPATH
logo_img = driver.find_element(By.XPATH, '//a[@class="a-link-nav-icon"]')

# Locate : Email field & send text, By ID
login_field = driver.find_element(By.ID, 'ap_email')
login_field.clear()
login_field.send_keys('abc@gmail.com')

# Locate : Continue button by CLASS NAME
continue_button = driver.find_element(By.CLASS_NAME, 'a-button-inner')

# Locate : Conditions of use link, By XPATH
condition_link = driver.find_element(By.XPATH, '//a[@href="/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088"]')

# Locate : Privacy Notice link, By XPATH
privacy_link = driver.find_element(By.XPATH, '//a[@href="/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496"]')

# Locate : Need help link, By XPATH
needhelp_link = driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-expand"]')
needhelp_link.click()
sleep(2)

# Forgot your password link
forgotpwd_link = driver.find_element(By.XPATH, '//*[@id="auth-fpp-link-bottom"]')

# Other issues with Sign-In link
otherlink_link = driver.find_element(By.XPATH, '//*[@id="ap-other-signin-issues-link"]')

# Create your Amazon account button
create_link = driver.find_element(By.XPATH, '//*[@id="createAccountSubmit"]')

sleep(4)