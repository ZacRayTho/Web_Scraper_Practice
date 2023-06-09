from bs4 import BeautifulSoup
import requests

with open("./WebScraper/index.html", "r") as f:
    # open syntax, first parameter is the file to open, second parameter is the mode 'r' means read mode
    # as f, f stands for file
    doc = BeautifulSoup(f, "html.parser")
    # beautfulSoup syntax, first parameter is document you want to read, and second parameter is the type of parser

# find_all makes a list of all tags with that tag name, can be accessed like a list/array 
# tag = doc.find_all("p")[1]
# you can grab nested tags too!
# print(tag.b)

# how to get a certain tag
# tag = doc.title
# tag.string will give only inside the tag
# print(tag)

# print(doc.prettify())
# .prettify() will format the html