from selenium import webdriver
import time

proxy = webdriver.FirefoxProfile()
proxy.set_preference("network.proxy.type", 1)
proxy.set_preference("network.proxy.http", "10.6.254.137")
proxy.set_preference("network.proxy.http_port", 8080)
profile.update_preferences()

driver = webdriver.firefox(Firefox_profile=profile)
driver.get("https://google.com")
time.sleep(2)
driver.close()