from bs4 import BeautifulSoup as soup #parsing HTML and XML documents
import requests #for http requests
from datetime import date

# getting current date information
today = date.today()
d = today.strftime("%Y-%m-%d")
#print("date= ", d)

jse_url = "https://www.jse.co.za/"
news = requests.get(jse_url)
stock_news = soup(news.content,'lxml')

for link in stock_news.findAll("main"):
    print("page:{}".format(link.text))


