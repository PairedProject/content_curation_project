from django.test import TestCase
from .models import Stocks
from django.contrib.auth import get_user_model

from django.conf import settings as django_settings
from importlib import import_module


# Create a class to enable adding session data to test client.
class SessionEnabledTestCase(TestCase):

    def get_session(self):
        if self.client.session:
            session = self.client.session
        else:
            engine = import_module(django_settings.SESSION_ENGINE)
            session = engine.SessionStore()
        return session

class StockAppTests(SessionEnabledTestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
				username = 'user1', 
				email = 'user1@gmail.com',
				password='secret',
				subscribed = True)
			
		self.stock_1 = Stocks.objects.create(
			ticker = 'AAPL',
			user = self.user)

		self.stock_2 = Stocks.objects.create(
			ticker = 'FB',
			user = self.user)

	def test_stock_exists(self):
		stock_list = Stocks.objects.all()
		self.assertEquals(stock_list.count(),2)
		self.assertEquals(stock_list[0].ticker, 'AAPL')
		self.assertEquals(self.user.stocks_set.all().count(), 2)

	def test_multiple_stocks_ass_to_user(self):
		self.assertEquals(self.user.stocks_set.all().count(), 2)

	def test_stock_detail_view_exists(self):
		session = self.get_session()
		session['meta_data'] = {'AAPL':{'ticker':'AAPL'}}
		session['price_data'] = {'AAPL':'AAPL'}
		session.save()
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get('/index/stock/AAPL')
		self.assertEquals(response.status_code, 200)

	def test_stock_detail_url_uses_correct_template(self):
		session = self.get_session()
		session['meta_data'] = {'AAPL':{'ticker':'AAPL'}}
		session['price_data'] = {'AAPL':'AAPL'}
		session.save()
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get('/index/stock/AAPL')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'stock_detail.html')

	def test_stock_delete_view_exists(self):
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get('/index/stock/AAPL/delete')
		self.assertEquals(response.status_code, 200)

	def test_stock_delete_url_uses_correct_template(self):
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get('/index/stock/AAPL/delete')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'stock_delete.html')

	def test_stock_is_deleted(self):
		stock_list = Stocks.objects.all()
		stock = stock_list[0]
		stock.delete()
		self.assertEquals(self.user.stocks_set.all().count(), 1)














































