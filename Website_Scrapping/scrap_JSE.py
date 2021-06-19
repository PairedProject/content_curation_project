from bs4 import BeautifulSoup
import requests
import json



top_stories = []

base_url = 'https://www.jse.co.za'

source = requests.get(base_url).text
print("Got source")

soup = BeautifulSoup(source, 'html.parser')
print("Parsed source")
articles = soup.find_all("article", class_="card")
print(f"Number of articles found: {len(articles)}")

for article in articles:
    try:
        headline = article.h3.text.strip()
        link = base_url + article.a['href']
        text = article.find("div", class_="field--type-text-with-summary").text.strip()
        img_url = base_url + article.picture.img['data-src']
        
        print(headline,link,text,img_url)
        
        
        stories_dict = {}
        stories_dict['Headline'] = headline
        stories_dict['Link'] = link
        stories_dict['Text'] = text
        stories_dict['Image'] = img_url
        
        top_stories.append(stories_dict)
        
    except AttributeError as ex:
        print('Error:',ex)
        
with open('top_stories.json','w')as f:
    json.dump(top_stories,f)
    
print('Fin.')

        
   
      
    
    
    
