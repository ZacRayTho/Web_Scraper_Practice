import csv
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.oreillyauto.com"
# driver.get(url)
# input()

def get_url(search_term):
    # Generate a url from search term
    template = "https://www.oreillyauto.com/search?q={}"
    search_term = search_term.replace(" ", "+")
    return template.format(search_term)
# https://www.oreillyauto.com/shop/b/bearings---seals/wheel-bearings-and-seals/wheel-bearing/5426c6f5d17c?q=wheel+bearing
url = get_url('wheel bearing')
print(url)

driver.get(url)



