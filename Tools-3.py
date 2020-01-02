from multiprocessing import Process
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
urls =['https://hvaandres.info','https://instgram.com' , 'https://youtube.com']

driver.get(urls[0])
for url in urls[1:]:
    driver.execute_script('window.open("{}", "_blank");'.format(url))
    print("You have your url list open")

