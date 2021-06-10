from bs4.builder import HTML
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
# web driver to access website on Chrome

driver = webdriver.Chrome()
driver.get('https://finance.yahoo.com/')
results = []
content = driver.page_source
# beautiful soup to parse the website 
soup = BeautifulSoup(content,'lxml')
# interating through the site pulling h3 tags with headlines.
for element in soup.find_all(attrs='main'):
    name = element.find('h3')
    if name not in results:
        results.append(name.text)
print(results)


