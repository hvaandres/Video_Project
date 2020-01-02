import csv
from selenium import webdriver
import time

# Script to open multiple links one by one through a CSV File!

def url_links(url_obj):
    reader = csv.DictReader(url_obj,delimiter = ',')
    for line in reader:
        url = line["url"]
        tittle = line["tittle"]
        print(url + tittle)
        chromedriver = '/Users/hvaandres/Desktop/Dev_Projects/QA_Testing/Project_Video/chromedriver'
        driver = webdriver.Chrome(chromedriver)
        driver.get(url)
        time.sleep(10)
        #assert tittle in driver.title
        driver.quit()
if __name__ == "__main__":
    with open ('/Users/hvaandres/Desktop/Dev_Projects/QA_Testing/Project_Video/URL.csv') as url_obj:
        url_links(url_obj)

# Script to open multiple links one by one with a time.sleep of 200 seconds

def url_links_200_seconds(url_obj):
    reader = csv.DictReader(url_obj,delimiter = ',')
    for line in reader:
        url = line["url"]
        tittle = line["tittle"]
        print(url + tittle)
        chromedriver = '/Users/hvaandres/Desktop/Dev_Projects/QA_Testing/Project_Video/chromedriver'
        driver = webdriver.Chrome(chromedriver)
        driver.get(url)
        time.sleep(200)
        #assert tittle in driver.title
        driver.quit()
if __name__ == "__main__":
    with open ('/Users/hvaandres/Desktop/Dev_Projects/QA_Testing/Project_Video/URL.csv') as url_obj:
        url_links_200_seconds(url_obj)

# Script to open multiple links one by one with a time.sleep of 200 seconds

   