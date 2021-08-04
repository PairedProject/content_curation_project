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
class Stocks(models.Model):
	ticker = models.CharField(max_length=5)
	user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.ticker

	def get_absolute_url(self):
		return reverse('pages:stock-detail', kwargs={'ticker': self.ticker})

	""" Api call to get current stock objects meta_data. """
	def get_meta_data(self):
		try:
			url = f'https://api.tiingo.com/tiingo/daily/{self.ticker}'
			response = requests.get(url, headers=headers)
			# Uncomment below to see price_data json object in terminal.
			# print(response.json())
			return response.json()
		#Handle error if user entered stock ticker does not exist.
		except KeyError:
			return {'ticker':self.ticker}

	""" Api call to get current stock objects price_data. """
	def get_price_data(self):
		try:
			url = f'https://api.tiingo.com/tiingo/daily/{self.ticker}/prices'
			response = requests.get(url, headers=headers)
			# Uncomment below to see price_data json object in terminal. 
			#print(response.json())
			return response.json()[0]
		#Handle error if user entered stock ticker does not exist.
		except KeyError:
			return {'high' : '   Invalid Ticker.'}
		except IndexError:
			return {'high': 'No Data'}
			










	