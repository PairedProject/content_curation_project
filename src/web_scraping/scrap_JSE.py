from bs4 import BeautifulSoup
import requests


def get_stories():
    """user agent to facilitates end-user interaction with web content"""

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
    }

    # Why did you choose the below data structure?
    # It will be hard to know which headline, link, image and text go together.
    # All headlines are in one list and all links in another.
    # You also need to think about how you would traverse the datastructure to display the info.
    # How would you loop over the items in the dictionary to print the headline, link, image and text for each article?

    top_stories = {"Headline": [], "Link": [], "Text": [], "Image": []}
    
    # I've found this data structure to be the easiest to work with...

    # top_stories = {'article1' : {'headline':'headline_1', 'link':'link_1, 'text':'text_1'},
    #                'aritcle2' : {'headline':'headline_2', 'link':'link_2, 'text':'text_2'},
    #                'article3' : {'headline':'headline_2', 'link':'link_2, 'text':'text_2'}}

    # You add to it like this top_stories['article1']['headline'] = article.h3.text.strip()
    #                         top_stories['article1']['link'] = base_url + article.a["href"]

    # top_stories['article1'] would return {'headline':'headline_1', 'link':'link_1, 'text':'text_1'}
    # And top_stories['article1']['headline'] would return 'headline_1'

    # You increase your arcticle number like this.
    # Initialise a count variable outside of your forloop. count = 1
    # Then inside your forloop you say top_stories[article + str(count)]['headline'] = article.h3.text.strip()
    # Then at the end of your forloop increase the count variable. count += 1
    
    
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

    # You need to return the top_stories data structure, not print it.
    # You return variables from functions and methods to use in other places.

    return top_stories
    #print(top_stories)

# If you wanted to test if it works you print the function to the screen or terminal.
# print(get_stories())
stories = get_stories()

# I've tried iterating through your current structure and  the only way I can see it working
# is to loop through the dictionary's keys and values using stories.items()
# And then loop through each item in the value list inside that loop.
# Nested loops are always the last resort as they have a BigO of n^2.

for key, value in stories.items():
    print(key)
    for index in range(0, len(value)):
        print(value[index])
    print()























