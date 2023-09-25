# import necessary libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# open a Google Chrome browser and call it 'browser'
browser = webdriver.Chrome()

# default email to use as username/email for logging in
my_email = "jacob.stuart@gtkycu.com"

# automatically upload Participation Tracking
def participation_tracking(user_ID, password):
    # go to TruStage
    browser.get('https://myservices.cunamutual.com/')
    
    # don't do anything until the page has loaded properly
    # we can tell it's loaded when the User ID is clickable
    # if it's not loaded after 4 seconds, throw TimeOutException
    wait = WebDriverWait(browser, 4)
    element = wait.until(EC.element_to_be_clickable((By.ID, "okta-signin-username")))

    # find username box
    user_ID_box = browser.find_element(By.ID, "okta-signin-username")
    # find password box
    pw_box = browser.find_element(By.ID, "okta-signin-password")

    # enter user ID
    user_ID_box.send_keys(user_ID)
    # enter password
    pw_box.send_keys(password)
    # click "Sign In"
    browser.find_element(By.ID, "okta-signin-submit").click()
    
    # need to deal with email verification

# automatically check online banking
def check_online_banking(user_ID, password):
    # go to GTKYCU's website
    browser.get('https://gtkycu.com/')

    # don't do anything until the page has loaded properly
    # we can tell it's loaded when the User ID is clickable
    # if it's not loaded after 4 seconds, throw TimeOutException
    wait = WebDriverWait(browser, 4)
    element = wait.until(EC.element_to_be_clickable((By.NAME, "UserName")))










def main():
    participation_tracking("jbstuart", "Frosty-Shelving83")
    
main()