from django.shortcuts import render
from users.models import CustomUser

from .models import Crypto

# Create your views here.

def crypto_detail_view(request, crypto_ticker):

	#crypto_ticker = request.user.crypto_set.get(crypto_ticker = crypto_ticker)

	instance = request.session['crypto_meta_data'][str(crypto_ticker)]
	price_data = request.session['crypto_price_data_dict'][str(crypto_ticker)]

	print(instance)

	context = {
		'instance' : instance,
		'price_data' : price_data,
	}
	return render(request, 'crypto_detail.html', context)


