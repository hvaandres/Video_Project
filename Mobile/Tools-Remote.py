from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
 'browser': 'Safari',
 'browser_version': '13.0',
 'os': 'OS X',
 'os_version': 'Catalina',
 'resolution': '1024x768'
}

driver = webdriver.Remote(
    command_executor='https://USERNAME:ACCESS_KEY@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
driver.quit()