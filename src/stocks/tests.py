from django.test import TestCase
from .models import Stocks
from django.contrib.auth import get_user_model

class StockAppTests(TestCase):

	username = 'newuser'
	email = 'newuser@gmail.com'
	subscribed = True

	def test_stock_exists(self):

		user = get_user_model().objects.create_user(
			username = self.username,
			email = self.email
			)

		stock = Stocks.objects.create(
			ticker = 'APPL',
			user = user)

		stock_list = Stocks.objects.all()
		self.assertEquals(stock_list.count(),1)
		self.assertEquals(stock_list[0].ticker, 'APPL')
		self.assertEquals(user.stocks_set.all().count(), 1)

	def test_multiple_stocks_ass_to_user(self):

		user = get_user_model().objects.create_user(
			username = self.username,
			email = self.email
			)

		stock_1 = Stocks.objects.create(
			ticker = 'APPL',
			user = user)
		stock_2 = Stocks.objects.create(
			ticker = 'FB',
			user = user)

		self.assertEquals(user.stocks_set.all().count(), 2)

