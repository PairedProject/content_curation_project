from django.db import models
from users.models import CustomUser
from django.urls import reverse

import requests

""" Request headers for api call. """
headers = {
	'Content-type' : 'Application/json',
	'Authorization' : 'Token 142f7a3ca629dc41d29be36e8e6751594e5dc57b'
}

"""
Create Stock Object
"""
class Crypto(models.Model):
	crypto_ticker = models.CharField(max_length=5)
	user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.crypto_ticker

	# def get_absolute_url(self):
	# 	return reverse('pages:stock-detail', kwargs={'ticker': self.ticker})

	""" Api call to get current stock objects meta_data. """
	def get_crypto_price_data(self):
		url = f"https://api.tiingo.com/tiingo/crypto/top?tickers={self.crypto_ticker}"
		response = requests.get(url, headers=headers)
		#print(response.json())
		return response.json()
		

	def get_crypto_meta_data(self):
		try:
			url = f'https://api.tiingo.com/tiingo/crypto?tickers={self.crypto_ticker}'
			response = requests.get(url, headers=headers)
			#print(response.json())
			return response.json()[0]
		except IndexError:
			return {'ticker': self.crypto_ticker}
		










	
