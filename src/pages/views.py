from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

from users.models import CustomUser
from stocks.models import Stocks
from crypto.models import Crypto
from .forms import TickerForm, CryptoTickerForm

""" Import get_stories() from scrap_JSE.py in web_scraping app"""
from web_scraping.scrap_JSE import get_stories

""" Define home_page_view as a function based view. """
def home_page_view(request):

	""" Set the variable jse_stories to the output of the function get_stories(). """
	jse_articles = get_stories()

	print(len(jse_articles))

	""" Add the jse_articles variable to the views context dictionary for use in the template. """
	context = {
		'jse_articles' : jse_articles,
	}
	return render(request, 'home.html', context)


""" Define user logged in page."""
def index_view(request):

	""" Create blank form instances. """
	form = TickerForm()
	crypto_form = CryptoTickerForm()
	
	""" Check if the request method == POST """
	if request.method == 'POST':
		post_data = request.POST or None
		""" Check that ther is data on the request """
		if post_data != None:
			""" Check if the user enters data and the stock ticker form. """
			if request.POST.get("form_type") == 'stock_form':
				form = TickerForm(request.POST)
				""" Check if form is valid. """
				if form.is_valid():
					""" Get the 'ticker' value from the form and store it the ticker variable. """
					ticker = form.cleaned_data.get('ticker')
					# If the variable ticker exists in the users portfolio send error message. """
					try: 
						if request.user.stocks_set.get(ticker=ticker) != None:
							messages.info(request, 'Stock ticker already exists in portfolio.')
					# Create the Stock Object in the database and link it to the current user.
					except Stocks.DoesNotExist:
						Stocks.objects.create(
							ticker = ticker, 
							user=request.user)
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
						crypto_form = CryptoTickerForm()
					


	""" Call a list of the users stocks and store it to be passed into the context. """
	stock_list = request.user.stocks_set.all()
	crypto_list = request.user.crypto_set.all()

	""" Initialse dictionaries to store meta data and price data. """
	stock_metadata_dict = {}
	stock_price_data_dict = {}

	crypto_metadata_dict = {}
	crypto_price_data_dict = {}

	""" 

	Loop through users stock and crypto portfolios and add meta and price data to respective dictionaries. 

	"""
	for stock in stock_list:
		stock_metadata_dict[stock.ticker] = stock.get_meta_data()
		stock_price_data_dict[stock.ticker] = stock.get_price_data()
		# Add stocks highest price data to meta data dict for use on index page.
		stock_metadata_dict[stock.ticker]['high'] = stock_price_data_dict[stock.ticker].get('high')
		stock_metadata_dict[stock.ticker]['ticker'] = stock.ticker

	for crypto in crypto_list:
		crypto_metadata_dict[crypto.crypto_ticker] = crypto.get_crypto_meta_data()
		crypto_price_data_dict[crypto.crypto_ticker] = crypto. get_crypto_price_data()

		crypto_metadata_dict[crypto.crypto_ticker]['topOfBookData'] = crypto_price_data_dict[crypto.crypto_ticker][0].get('topOfBookData')

	""" Set session variables for meta and price data to be used throughout site. """
	request.session['meta_data'] = stock_metadata_dict
	request.session['price_data'] = stock_price_data_dict

	request.session['crypto_meta_data'] = crypto_metadata_dict
	request.session['crypto_price_data_dict'] = crypto_price_data_dict

	#print(request.session['crypto_meta_data']['ethusd']['ticker'])
	
	context = {
		'form' : form,
		'crypto_form' : crypto_form,
	}

	return render(request, 'index.html', context)

	


