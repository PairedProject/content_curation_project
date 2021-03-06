from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

from users.models import CustomUser
from stocks.models import Stocks
from crypto.models import Crypto
from .forms import TickerForm, CryptoTickerForm

# Import get_stories() from scrap_JSE.py in web_scraping app.
from web_scraping.scrap_JSE import get_stories
from web_scraping.coin_desk import crypto_news


def home_page_view(request):
	""" Define home_page_view as a function based view. """

	# Set the variable jse_articles to the output of the function get_stories().
	jse_articles = get_stories()
	# Commenting the below out due to 404 error on site
	#coindesk_articles = crypto_news()

	# Add the jse_articles variable to the views context dictionary for use in the template.
	context = {
		'jse_articles' : jse_articles,	
		#'coindesk_articles': coindesk_articles,
	}
	return render(request, 'home.html', context)



def index_view(request):
	""" 
	Define user logged in page where they are able to add tickers to their portfolio and view displayed
	information for those tickers.
	"""

	# Create blank form instances.
	form = TickerForm()
	crypto_form = CryptoTickerForm()
	
	# Check if the request method == POST
	if request.method == 'POST':
		post_data = request.POST or None
		# Check that ther is data on the request.
		if post_data != None:
			# Check if the user enters data and the stock ticker form.
			if request.POST.get("form_type") == 'stock_form':
				form = TickerForm(request.POST)
				# Check if form is valid.
				if form.is_valid():
					# Get the 'ticker' value from the form and store it the ticker variable.
					ticker = form.cleaned_data.get('ticker')
					# If the variable ticker exists in the users portfolio send error message.
					try: 
						if request.user.stocks_set.get(ticker=ticker) != None:
							messages.info(request, 'Stock ticker already exists in portfolio.')
					# Create the Stock Object in the database and link it to the current user.
					except Stocks.DoesNotExist:
						Stocks.objects.create(
							ticker = ticker, 
							user=request.user)
						# Get the stock that was created from the database.
						current_stock = Stocks.objects.get(ticker=ticker, user=request.user)
						# Get the meta and price data
						current_stock_meta_dict = current_stock.get_meta_data()
						current_stock_price_dict = current_stock.get_price_data()
						# Add the highest price for the stock to the meta data dict
						current_stock_meta_dict['high'] = current_stock_price_dict.get('high')
						# Add a ticker variable to meta data incase user enters incorrect ticker and there is no data.
						current_stock_meta_dict['ticker'] = current_stock.ticker
						# Add the meta and price data to the current session
						request.session['meta_data'][current_stock.ticker] = current_stock_meta_dict
						request.session['price_data'][current_stock.ticker] = current_stock_price_dict
						# Explicitly save the session
						request.session.modified = True
						# Reset the form instance.
						form = TickerForm()


			# Check wether the user enters data on the crypto currency ticker form.
			elif request.POST.get("form_type") == 'crypto_form':
				crypto_form = CryptoTickerForm(request.POST)
				if crypto_form.is_valid():
					crypto_ticker = request.POST['crypto_ticker']
					# If the variable crypto_ticker exists in the users portfolio send error message.
					try:
						if request.user.crypto_set.get(crypto_ticker=crypto_ticker) != None:
							messages.info(request, 'Crypto ticker already exists in portfolio.')
					# Else create the Crypto Object in the database and link it to the current user.
					except Crypto.DoesNotExist:
						Crypto.objects.create(
							crypto_ticker = crypto_ticker, 
							user=request.user)
						# Get the currently created cryptocurrency ticker
						current_crypto = Crypto.objects.get(crypto_ticker = crypto_ticker, user = request.user)
						# Get the meta data and price data for the current cryptocurrency
						current_crypto_meta_dict = current_crypto.get_crypto_meta_data()
						current_crypto_price_dict = current_crypto.get_crypto_price_data()
						# Add a crypto_ticker variable to meta data incase user enters incorrect ticker and there is no data.
						current_crypto_meta_dict['crypto_ticker'] = current_crypto.crypto_ticker
						# Handle Error for no data on creation of invalid cryptocurrency object
						if len(current_crypto_price_dict) == 0:
							current_crypto_price_dict.append({'topOfBookData':[{'lastPrice':'No_Data'}]})

						# Add the meta data and price data to the current session
						request.session['crypto_meta_data'][current_crypto.crypto_ticker] = current_crypto_meta_dict
						request.session['crypto_price_data_dict'][current_crypto.crypto_ticker] = current_crypto_price_dict
						# Save the session
						request.session.modified = True
						# Reset the crypto_form
						crypto_form = CryptoTickerForm()
					


	#Call a list of the users stocks and store it to be passed into the context.
	stock_list = request.user.stocks_set.all()
	crypto_list = request.user.crypto_set.all()

	# Initialse dictionaries to store meta data and price data.
	stock_metadata_dict = {}
	stock_price_data_dict = {}

	crypto_metadata_dict = {}
	crypto_price_data_dict = {}

	# Loop through users stock and crypto portfolios and add meta and price data to respective dictionaries. 

	# Only do this the first time the user logs into the site.
	if request.session.get('meta_data') == None:
		for stock in stock_list:
			stock_metadata_dict[stock.ticker] = stock.get_meta_data()
			stock_price_data_dict[stock.ticker] = stock.get_price_data()
			# Add stocks highest price data to meta data dict for use on index page.
			stock_metadata_dict[stock.ticker]['high'] = stock_price_data_dict[stock.ticker].get('high')
			# Add a ticker to metadata dict incase user enters incorrect ticker and there is no data returned.
			stock_metadata_dict[stock.ticker]['ticker'] = stock.ticker

		for crypto in crypto_list:
			crypto_metadata_dict[crypto.crypto_ticker] = crypto.get_crypto_meta_data()
			crypto_price_data_dict[crypto.crypto_ticker] = crypto.get_crypto_price_data()
			# Add a crypto_ticker to metadata dict incase user enters incorrect ticker and there is no data returned.
			crypto_metadata_dict[crypto.crypto_ticker]['crypto_ticker'] = crypto.crypto_ticker
			# Handle error when there is no data recieved for an incorrect ticker.
			if len(crypto_price_data_dict[crypto.crypto_ticker]) == 0:
				crypto_price_data_dict[crypto.crypto_ticker] = [{'topOfBookData':[{'lastPrice':'No Data'}]}]
	
		# Set session variables for meta and price data to be used throughout site.
		request.session['meta_data'] = stock_metadata_dict
		request.session['price_data'] = stock_price_data_dict

		request.session['crypto_meta_data'] = crypto_metadata_dict
		request.session['crypto_price_data_dict'] = crypto_price_data_dict
	
	context = {
		'form' : form,
		'crypto_form' : crypto_form,
	}

	return render(request, 'index.html', context)

	


