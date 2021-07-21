from bs4 import BeautifulSoup
import requests

def get_investopidia_articles():

        source = requests.get('https://www.investopedia.com/company-news-4427705').text

        #print(source)

        soup = BeautifulSoup(source, 'lxml')

        #print(soup.prettify())

        # Initialise dictionary to store articles
        article_dict = {}
        # Initailse article count
        count = 1
        for item in soup.find_all('li', class_='card-list__item')[0:3]:
        
                text = item.find('span', class_="card__title-text").text
                # Add the key, article1 to the article_dict and set its value to
                # the dictionary {"Headline":text}
                article_dict["article"+str(count)] = {"Headline":text}
                img = item.find('a', class_='card--featured').div.img['data-src']
                # Add the key "img" and the value img to the article1 dictionary
                article_dict["article"+str(count)]["img"] = img
                link = item.find('a')
                article_link = link.attrs['href']
                # Add the key "link" and the value article_link to the article1 dictionary
                article_dict["article"+str(count)]["link"] = article_link
                # Increase article counter
                count += 1

        return article_dict



# investopidia_articles = (get_investopidia_articles())

# print("DICTIONARY OF ARTICLE DICTIONARIES")
# print(investopidia_articles)

# print("__________________________________")

# for k,v in investopidia_articles.items():
#         print("Headline \n" + str(v["Headline"]) + "\n" + "Article Link \n" + str(v["link"]) + "\n" + "Image Link \n" + str(v["img"]) + "\n")
                


