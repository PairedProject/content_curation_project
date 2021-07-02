from django.shortcuts import render, redirect
from users.models import CustomUser
from .models import Stocks

""" Detail view for displaying stock instance details. """
def stock_detail_view(request, ticker):
	""" Call the meta data for the stock instance from the saved session variable. """
	instance = request.session['meta_data'][ticker]
	""" Call the price data for the stock instance from the saved session variable. """
	price_data = request.session['price_data'][ticker]

	context = {
		'instance': instance,
		'price_data': price_data,
	}
	return render(request, 'stock_detail.html', context) 

""" Delete view for deleting a stock instance. """
def stock_delete_view(request, ticker):

	""" Get the instance from the users portfolio. """
	stock = request.user.stocks_set.get(ticker=ticker)

	""" Check if user clicked confirm, delete and redirect. """
	if request.method == 'POST':
		stock.delete()
		del request.session['meta_data'][ticker]
		del request.session['price_data'][ticker]
		request.session.modified = True
		""" Redirect user to index page once delete is successful. """
		return redirect('pages:index')

	context = {
		'stock' : stock,
	}

	return render(request, 'stock_delete.html', context)
