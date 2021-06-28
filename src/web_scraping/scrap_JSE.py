from bs4 import BeautifulSoup
import requests


top_stories = []


def get_stories():
    """ user agent to facilitates end-user interaction with web content"""

    headers = {
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }

    base_url = 'https://www.jse.co.za/'

    source = requests.get(base_url).text

    soup = BeautifulSoup(source, 'html.parser')

    articles = soup.find_all("article", class_="card")
    print(f"Number of articles found: {len(articles)}")

    for article in articles:
        try:
            headline = article.h3.text.strip()
            link = base_url + article.a['href']
            text = article.find(
                "div", class_="field--type-text-with-summary").text.strip()
            img_url = base_url + article.picture.img['data-src']

            # print(headline, link, text, img_url)

            stories_dict = {}
            stories_dict['Headline'] = headline
            stories_dict['Link'] = link
            stories_dict['Text'] = text
            stories_dict['Image'] = img_url

            top_stories.append(stories_dict)

        except AttributeError as ex:
            print('Error:', ex)
    return top_stories





