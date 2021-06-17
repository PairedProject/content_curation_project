from bs4 import BeautifulSoup
import requests

base_url = 'https://www.jse.co.za'

source = requests.get(base_url).text
print("Got source")

soup = BeautifulSoup(source, 'html.parser')
print("Parsed source")

articles = soup.find_all("article", class_="card")
print(f"Number of articles found: {len(articles)}")

for article in articles:
    print("----------------------------------------------------")

    headline = article.h3.text.strip()
    link = base_url + article.a['href']
    text = article.find("div", class_="field--type-text-with-summary").text.strip()
    img_url = base_url + article.picture.img['data-src']

    print(headline)
    print(link)
    print(text)
    print("Image: "+ img_url)
