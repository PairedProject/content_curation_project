from bs4 import BeautifulSoup
import requests


def get_stories():
    """user agent to facilitates end-user interaction with web content"""

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
    }

    top_stories = {"Headline": [], "Link": [], "Text": [], "Image": []}
    base_url = "https://www.jse.co.za/"

    source = requests.get(base_url, headers=headers).text

    soup = BeautifulSoup(source, "html.parser")

    articles = soup.find_all("article", class_="card")
    print(f"Number of articles found: {len(articles)}")

    for article in articles:
        try:
            top_stories["Headline"].append(article.h3.text.strip())
            top_stories["Link"].append(base_url + article.a["href"])
            top_stories["Text"].append(
                article.find("div", class_="field--type-text-with-summary").text.strip()
            )
            top_stories["Image"].append(base_url + article.picture.img["data-src"])

        except AttributeError as ex:
            print("Error:", ex)

    #print(type(top_stories))
    print(top_stories)


get_stories()
