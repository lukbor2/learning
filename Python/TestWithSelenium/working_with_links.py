from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://www.ghirardelli.com/")
#time.sleep(5)

print("Page Title: ", driver.title)

links = driver.find_elements_by_tag_name('a')
print("Found " ,len(links), " links in the page.")

driver.quit() #closes the browser window opened by webdriver.
