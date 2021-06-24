from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

from users.models import CustomUser
from stocks.models import Stocks
from crypto.models import Crypto
from .forms import TickerForm, CryptoTickerForm

# Create landing page
class HomePageView(TemplateView):
	template_name = 'home.html'


""" Define user logged in page."""
def index_view(request):

	""" Create blank form instance. """
	form = TickerForm()
	crypto_form = CryptoTickerForm()
	
	""" Check if theres data on the post request and if there is pass it to the Tickerform() instance."""
	if request.method == 'POST':
		post_data = request.POST or None
		if post_data != None:
			if request.POST.get("form_type") == 'stock_form':
				form = TickerForm(request.POST)
				""" Check if form is valid. """
				if form.is_valid():
					""" If it is get the 'ticker' value from the form and store it the ticker variable. """
					ticker = form.cleaned_data.get('ticker')
					# If the variable ticker exists in the users portfolio send error message.
					try: 
						if request.user.stocks_set.get(ticker=ticker) != None:
							messages.info(request, 'Stock ticker already exists in portfolio.')
					# Else create the Stock Object in the database and link it to the current user. """
					except Stocks.DoesNotExist:
						Stocks.objects.create(
							ticker = ticker, 
							user=request.user)

			elif request.POST.get("form_type") == 'crypto_form':
				crypto_form = CryptoTickerForm(request.POST)
				if crypto_form.is_valid:
					crypto_ticker = request.POST['crypto_ticker']
					try: 
						if request.user.crypto_set.get(crypto_ticker=crypto_ticker) != None:
							messages.info(request, 'Crypto ticker already exists in portfolio.')
					# Else create the Stock Object in the database and link it to the current user. """
					except Crypto.DoesNotExist:
						Crypto.objects.create(
							crypto_ticker = crypto_ticker, 
							user=request.user)
					


	""" Call a list of the users stocks and store it to be passed into the context. """
	stock_list = request.user.stocks_set.all()
	crypto_list = request.user.crypto_set.all()

	""" Initialse dictionaries to store meta data and price data. """
	stock_metadata_dict = {}
	stock_price_data_dict = {}

	crypto_metadata_dict = {}
	crypto_price_data_dict = {}

	""" Loop through users stock portfolio and add meta and price data to respective dictionaries. """
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

	print(crypto_metadata_dict)
	print()
	print(crypto_price_data_dict)
		

	""" Set session variables for meta and price data to be used throughout site. """
	request.session['meta_data'] = stock_metadata_dict
	request.session['price_data'] = stock_price_data_dict

	request.session['crypto_meta_data'] = crypto_metadata_dict
	request.session['crypto_price_data_dict'] = crypto_price_data_dict

	
	context = {
		'form' : form,
		'crypto_form' : crypto_form,
	}

	return render(request, 'index.html', context)

	


