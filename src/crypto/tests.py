from django.test import TestCase
from .models import Crypto
from django.contrib.auth import get_user_model

from django.conf import settings as django_settings
from importlib import import_module

from stocks.tests import SessionEnabledTestCase

# Create your tests here.

class CryptoAppTests(SessionEnabledTestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
				username = 'user1', 
				email = 'user1@gmail.com',
				password='secret',
				subscribed = True)
			
		self.crypto_1 = Crypto.objects.create(
			crypto_ticker = 'btcusd',
			user = self.user)

		self.crypto_2 = Crypto.objects.create(
			crypto_ticker = 'ethusd',
			user = self.user)

	def test_crypto_object_exists(self):
		crypto_list = Crypto.objects.all()
		count = crypto_list.count()
		self.assertEquals(count, 2)

	def test_multiple_cryptocurrencies_assoc_to_one_user(self):
		self.assertEquals(self.user.crypto_set.all().count(), 2)


	def test_crypto_detail_view_exists(self):
		session = self.get_session()
		session['crypto_meta_data'] = {'btcusd': 'btcusd'}
		session['crypto_price_data_dict'] = {'btcusd':'btcusd'}
		session.save()
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get('/index/crypto/btcusd')
		self.assertEquals(response.status_code, 200)

	def test_crypto_detail_url_uses_correct_template(self):
		session = self.get_session()
		session['crypto_meta_data'] = {'btcusd': 'btcusd'}
		session['crypto_price_data_dict'] = {'btcusd':'btcusd'}
		session.save()
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get('/index/crypto/btcusd')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'crypto_detail.html')
















