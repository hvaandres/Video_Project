import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading


# This example will help us to open a video on youtube and skip the ads

options = webdriver.ChromeOptions() 
 
class ChromeTime(unittest.TestCase):
 
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument("disable-popup-blocking")
        #chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome("/Users/hvaandres/Desktop/Dev_Projects/QA_Testing/Project_Video/chromedriver", options=chrome_options) #/usr/local/bin/chromedriver - Linux Machine
        self.driver.maximize_window()  
  
    def testing3(self):
        driver_chrome = self.driver

        driver_chrome.get("https://youtube.com")
        print("Opening Youtube")
        driver_chrome.find_element_by_name("search_query").send_keys("peter mckinnon")
        print("Looking for the youtuber")
        driver_chrome.find_element_by_id("search-icon-legacy").click()
        print("Finally, we found your youtuber!")
        time.sleep(5)
        driver_chrome.find_element_by_class_name("style-scope ytd-vertical-list-renderer").click()
        print("Trying to open thee video that you would like to watch")
        time.sleep(10)
        driver_chrome.find_element_by_class_name("ytp-ad-skip-button-container").click()
        print("You're skipping the ads")
        time.sleep(10)
        driver_chrome.find_element_by_class_name("ytp-popup ytp-settings-menu").click()
        time.sleep(10)

        print("Initial Page Title is : %s" %driver_chrome.title)
        windows_before  = driver_chrome.current_window_handle
        print("First Window Handle is : %s" %windows_before)


# Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser. 
        self.driver.close()
 
if __name__ == "__main__":
    unittest.main() 