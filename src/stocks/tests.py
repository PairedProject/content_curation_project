from django.test import TestCase
from .models import Stocks
from django.contrib.auth import get_user_model

class StockAppTests(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
				username = 'user1', 
				email = 'user1@gmail.com',
				password='secret',
				subscribed = True)
			
		self.stock_1 = Stocks.objects.create(
			ticker = 'APPL',
			user = self.user)

		self.stock_2 = Stocks.objects.create(
			ticker = 'FB',
			user = self.user)

	def test_stock_exists(self):
		stock_list = Stocks.objects.all()
		self.assertEquals(stock_list.count(),2)
		self.assertEquals(stock_list[0].ticker, 'APPL')
		self.assertEquals(self.user.stocks_set.all().count(), 2)

	def test_multiple_stocks_ass_to_user(self):
		self.assertEquals(self.user.stocks_set.all().count(), 2)

	def test_stock_detail_view_exists(self):
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get('/index/APPL')
		self.assertEquals(response.status_code, 200)

	def test_stock_detail_url_uses_correct_template(self):
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get('/index/APPL')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'stock_detail.html')

	def test_stock_delete_view_exists(self):
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get('/index/APPL/delete')
		self.assertEquals(response.status_code, 200)

	def test_stock_delete_url_uses_correct_template(self):
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get('/index/APPL/delete')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'stock_delete.html')

	def test_stock_is_deleted(self):
		stock_list = Stocks.objects.all()
		stock = stock_list[0]
		stock.delete()
		self.assertEquals(self.user.stocks_set.all().count(), 1)














































