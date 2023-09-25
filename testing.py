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

def get_element(driver, by, keyword):
    # wait until the page has loaded properly,
    # when the specified ID is visible
    wait = WebDriverWait(driver, 5)

    if by == "ID" or by == "id" or by == "Id" or by == "iD":
        # returns the element that has the corresponding ID
        element = wait.until(EC.presence_of_element_located((By.ID, keyword)))
    elif by == "NAME" or by == "Name" or by == "name":
        # returns the element that has the corresponding ID
        element = wait.until(EC.presence_of_element_located((By.NAME, keyword)))
    
    return element

# automatically upload Participation Tracking
def participation_tracking(user_ID, password):
    # go to TruStage/CUNA
    browser.get('https://myservices.cunamutual.com/')
    
    # find username box
    user_ID_box = get_element(browser, ID, "okta-signin-username")
    # find password box
    pw_box = get_element(browser, ID, "okta-signin-password")

    # enter user ID
    user_ID_box.send_keys(user_ID)
    # enter password
    pw_box.send_keys(password)
    # click "Sign In"
    get_element(browser, "okta-signin-submit").click()
    
    # need to deal with email verification

# automatically check online banking
def check_online_banking(user_ID, password):
    # go to GTKYCU's website
    browser.get('https://gtkycu.com/')

    # get the user ID
    user_ID = get_element(browser, NAME, "UserName")
    # get the password
    pw = get_element(browser, NAME, "Password")
    
# automatically dial main line
def check_phone_status(username, password):
    browser.get('https://login.windstream.com/idp/startSSO.ping?PartnerSpId=https%3A%2F%2Flogin.windstream.com&loginAdapterId=myBusinessWeb&TargetResource=https://mybusiness.gokinetic.com/account/pingauth/po3login')

     # don't do anything until the page has loaded properly
    # we can tell it's loaded when the User ID is clickable
    # if it's not loaded after 4 seconds, throw TimeOutException
    wait = WebDriverWait(browser, 4)
    element = wait.until(EC.presence_of_element_located((By.NAME, "UserName")))

def main():
    #participation_tracking("jbstuart", "Frosty-Shelving83")
    check_online_banking("TestAccount2", "Twisty-Denial-Hymn80")

main()