from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.oreillyauto.com/'
driver.get(url)
# doc = BeautifulSoup(result.text, 'html.parser')
# print(doc.prettify())