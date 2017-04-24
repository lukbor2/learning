import requests
import time
from bs4 import BeautifulSoup


def get_urls(page):
    #returns a list of non-duplicated urls from the page.
    r = requests.get(page)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    urls_all = [link.get('href') for link in links if link.get('href') and link.get('href')[0:4]=='http']
    urls = list(set(urls_all)) #removing duplicates
    return urls

def process_list(urls):
    #processes a list of urls passed as argument and returns a list of urls found.
    urls_to_check = []
    for url in urls:
        urls = get_urls(url)
        urls_to_check += urls
    return urls_to_check

def check_urls(urls):
    results = []
    for url in urls:
        print("Now Processing: " + str(url) + "\n")
        r = requests.get(url)
        try:
            r.raise_for_status()
            result = (r.status_code, r.history, url, 'OK')
        except HTTPError:
            result = (r.status_code, [], url, "ERROR!")
        results.append(result)
    return results

if __name__ == "__main__":
    file_name = 'links_check.txt' #name of the text file where results are written.
    site = 'https://www.ghirardelli.com'
    urls_list = []
    urls_list.append(site) #starting point is just the url of the site.
    urls_to_check = [] #this is where I store all the urls which will have to be checked.
    depth = 1 #I use this variable to control how many iterations I will do. i.e. how deep in the tree I will go to check the links.
    i = 0
    while i < depth:
        urls = process_list(urls_list)
        urls_to_check += urls
        urls_list = urls
        i += 1
    urls_to_check = list(set(urls_to_check)) #removing duplicates

    try:
        f = open(file_name, 'w')
    except OSError:
        print('ERROR opening the file where to write results.')

    for result in urls_to_check:
        f.write(str(result) + '\n')

    time_start = time.time()
    for result in check_urls(urls_to_check):
        f.write(str(result) + '\n')
    time_end = time.time()
    print("Execution time - Version 2: " + time_start - time_end)

    f.close()
