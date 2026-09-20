#Look at this link to learn about checking broken links
# https://www.webucator.com/blog/2016/05/checking-your-sitemap-for-broken-links-with-python/

#I start from a url. Collect all the links in that page looking at 'a' tag.
#Then I remove the links which do not have any href attribute.
#Then I request all url and check the request status.
#The results are written to a text file.

import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://www.ghirardelli.com/")
file_name = 'links_check.txt' #name of the text file where results are written.

print("Page Title: ", driver.title)

links = driver.find_elements_by_tag_name('a')
print("Found " ,len(links), " links in the page.")

links = [l for l in links if l.get_attribute("href")] #removing the links which do not have any href.
print("Remaining links afer removing nulls: " ,len(links))

urls_all = []
for link in links:
    urls_all.append(link.get_attribute("href"))
    print(link.get_attribute("href"))
urls = list(set(urls_all)) #removing the duplicated urls in the list, if any.

print("Remaining links afer removing duplicates: " ,len(urls))

results = []
for url in urls:
    try:
        r = requests.get(url)
        #report = str(r.status_code) # returns the status code of the http request
        if r.history:
            history_status_codes = [str(h.status_code) for h in r.history]
            #report += ' [HISTORY: ' + ', ' .join(history_status_codes) + ']'
            result = (r.status_code, r.history, url, 'Success. Redirect to ' + r.url)
        elif r.status_code == 200:
            result = (r.status_code, r.history, url, 'Success. No Redirect')
        else:
            result = (r.status_code, r.history, url, 'ERROR')
    except Exception as e:
        result = (0, [], url, e)

    results.append(result)
try:
    f = open(file_name, 'w')
except OSError:
    print('ERROR opening the file where to write results.')

for result in results:
    f.write(str(result) + '\n')

driver.quit() #closes the browser window opened by webdriver.
