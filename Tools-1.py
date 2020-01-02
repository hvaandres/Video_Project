
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time



driver = webdriver.Chrome(executable_path="/Users/hvaandres/Desktop/Dev_Projects/QA_Testing/Project_Video/chromedriver")

# driver.execute_script("window.open('https://google.com', 'https://gmail.com', 'https://twitter.com')")
# driver.switch_to.window

#1
driver.get("http://msn.com")


#2
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.switch_to.window(driver.window_handles[0])
driver.get("http://cnn.com")


#3
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.switch_to.window(driver.window_handles[-1])
driver.get("http://www.yahoo.com")


#4
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.switch_to.window(driver.window_handles[0])
driver.get("https://www.apple.com")


#5
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.switch_to.window(driver.window_handles[0])
driver.get("https://www.google.com")

#6
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.switch_to.window(driver.window_handles[0])
driver.get("https://www.stackoverflow.com")


driver.quit()
