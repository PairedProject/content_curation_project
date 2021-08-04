# content_curation_project

PROJECT DESCRIPTION: 

This project aims to build a financial content curation site that users can visit to get the latest financial news in one place.
Users will be able to log in to the site where they will be able to add stocks and cryptocurrencies to their basket. 
The basket will display the latest price data for each stock and cryptocurrency inside it. 
Users will be able to click on the stock ticker to visit a detail page where all the meta data and price data for that particular stock or cryptocurrency is displayed.

CURRENT PROGRESS:

   So far, the site is working but can have long loading times.
   Error handling is also not complete as their are a few edge cases still to be fixed.
   Testing is ongoing, but I have not been able to get all my tets to pass yet as I am having a problem with sessions and django's test client.
   API testing is still to be implemented as research into it is ongoining.
   
ROADMAP:

Homepage:

  The home page will display a selection of news articles scraped from various sites on the web. 
  There will be a headline and image in a card with links to the website on which the article is on.
  
Index page:

   The index page is what the user will see after they signup and log in. 
   There will be two seperate forms for adding a stock ticker and a cryptocurrency ticker to thier basket.
   Once added to the users basket, the site will automatically pull the price and meta data for the added ticker and display the highest price for the day.
   Users will be able to click on the ticker in their basket and be taken to a page that displays all the information for the selected ticker.
   
   Currently the site makes the api call that retrieves that data everytime the homepage is loaded which causes it to be a bit slow.
   The solution to this is to add all the data to the session dictionary when the page is first loaded and then just update the dictionary whenver there is a change in the users basket.
   The implemantation of this solution is ongoing though...
   The user also has to refresh the entire page to update the information.
   In future, a refresh button will be added to the basket using javascript and and the basket will be able to be updated asyncronously.
   
 Detail Page:
 
   The detail page displays all the current price data and meta data for the chosen ticker.
   This is also where users can come to delete a ticker from their basket.
   Once the user decides to delete the ticker they will be taken to a confirmation page asking them to confirm the deletion.
   In future there will be a trash icon in the users basket where they can delete a ticker asycronously.
   
 Newsletter:
 
  The site will also have a newsletter which the user can subscribe to.
  It will contain links to news specific to the tickers in their basket.
  Users can choose to subscribe when they signup or at anytime during their visit.
  They will also be able to unsubscribe at any time.
