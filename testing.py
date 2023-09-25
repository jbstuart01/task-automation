# import necessary libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# open a Google Chrome browser and call it 'browser'
browser = webdriver.Chrome()

# default email to use as username/email for logging in
my_email = "jacob.stuart@gtkycu.com"

# returns a web element, "by" = type of field, "keyword" = unique ID
def get_element(by, keyword):
    # wait until the page has loaded properly,
    # when the specified ID is visible
    wait = WebDriverWait(browser, 5)

    if by == "ID" or by == "id" or by == "Id" or by == "iD":
        # returns the element that has the corresponding ID
        element = wait.until(EC.presence_of_element_located((By.ID, keyword)))
    elif by == "NAME" or by == "Name" or by == "name":
        # returns the element that has the corresponding ID
        element = wait.until(EC.presence_of_element_located((By.NAME, keyword)))
    elif by == "CLASS" or by == "class" or by == "Class":
        # returns the element that has the corresponding ID
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, keyword)))
    elif by == "TAG" or by == "tag" or by == "Tag":
        # returns the element that has the corresponding ID
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, keyword)))

    return element

# upload Participation Tracking
def participation_tracking(user_ID, password):
    # go to TruStage/CUNA
    browser.get('https://myservices.cunamutual.com/')
    
    # find username box
    user_ID_box = get_element(browser, "ID", "okta-signin-username")
    # find password box
    pw_box = get_element(browser, "ID", "okta-signin-password")

    # enter user ID
    user_ID_box.send_keys(user_ID)
    # enter password
    pw_box.send_keys(password)
    # click "Sign In"
    get_element(browser, "okta-signin-submit").click()
    
    # need to deal with email verification

# check online banking
def check_online_banking(user_ID, password):
    # go to GTKYCU's website
    browser.get('https://gtkycu.com/')

    # get the user ID
    user_ID_box = get_element(browser, "NAME", "UserName")
    # get the password
    pw = get_element(browser, "NAME", "Password")

    # get the right side "Online Banking" menu
    get_element(browser, "CLASS", "olbIcon").moveToElement()

    # enter the username and password
    user_ID_box.send_keys(user_ID)
    pw.send_keys(password)

    time.sleep(3)

# dial main line
def check_phone_status(username, password):
    # go to OfficeSuite
    browser.get('https://login.windstream.com/idp/startSSO.ping?PartnerSpId=https%3A%2F%2Flogin.windstream.com&loginAdapterId=myBusinessWeb&TargetResource=https://mybusiness.gokinetic.com/account/pingauth/po3login')

    # enter username and password
    get_element("ID", "username").send_keys(username)
    get_element("ID", "password").send_keys(password)

    # click sign on button
    get_element("ID", "signOnButton").click()    
    # click "Go To OfficeSuite"
    get_element("CLASS", "smb-btn-primary").click()
    # click "Dialpad"
    #get_element("TAG", "dialpad").moveToElement()
    time.sleep(5)


def main():
    #participation_tracking("jbstuart", "Frosty-Shelving83")
    #check_online_banking("TestAccount2", "Twisty-Denial-Hymn80")
    check_phone_status(my_email, "Dusty-Star-Fire34")
main()