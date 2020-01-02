
import csv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time





def url_links(url_obj):
    reader = csv.DictReader(url_obj,delimiter = ',')
    try: 
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--incognito")
        
        for line in reader:
            url = line["url"]
            tittle = line["tittle"]
            print(url + tittle)
            chromedriver = '/usr/local/bin/chromedriver' 
            driver = webdriver.Chrome(chromedriver, options=chrome_options) 
            driver.get(url)
            time.sleep(10)
            driver.quit()
#assert tittle in driver.title

    except:

        print("everything ready")

    finally:

        print("everything ready")

if __name__ == "__main__":
    with open ('/home/oem/Desktop/Video_Project-master/URL.csv') as url_obj:
        url_links(url_obj)
