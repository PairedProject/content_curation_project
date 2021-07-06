from bs4 import BeautifulSoup
import requests


def crypto_news():
    
    crypto_headlines = []
    
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
    }




    base_url ='https://www.coindesk.com/news'

    source = requests.get(base_url).text

    soup = BeautifulSoup(source, "html.parser")       
    
    
    articles = soup.find_all(class_ = 'text-content')
    
#print(len(articles))
#print(articles) 

    
    for article in articles:
        try:
            headline = article.h4.text.strip()
            link = base_url + article.a['href']
            text = article.find(class_="card-text").text.strip()
            # img_url = base_url + article.picture.img['src'] 
           
            crypto_dict = {}
            crypto_dict['Headline'] = headline
            crypto_dict['Link'] = link
            crypto_dict['Text'] = text
            
            
            crypto_headlines.append(crypto_dict)
            
            
        except AttributeError as ex:
            print('Error:', ex)
            
            
    return crypto_headlines

            
        


            
          


    

 



    

