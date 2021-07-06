from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from stocks.models import Stocks
from users.models import CustomUser

from .forms import TickerForm, CryptoTickerForm

class HomePageTests(SimpleTestCase):

	def test_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEquals(response.status_code, 200)

	def test_view_url_by_name(self):
		response = self.client.get(reverse('pages:home'))
		self.assertEquals(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('pages:home'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')

class IndexPageTests(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
				username = 'user1', 
				email = 'user1@gmail.com',
				password='secret',
				subscribed = True)
			
		self.ticker = Stocks.objects.create(
			ticker = 'APPL',
			user = self.user)

	def test_index_page_exists(self):
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get('/index/')
		self.assertEquals(response.status_code, 200)

	def test_view_url_by_name(self):
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get(reverse('pages:index'))
		self.assertEquals(response.status_code, 200)

	def test_url_uses_correct_template(self):
		user = self.client.login(username = 'user1', password='secret')
		response = self.client.get(reverse('pages:index'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')

	def test_post_content(self):
		self.assertEquals(f'{self.ticker}', 'APPL')
		self.assertEquals(f'{self.user}', 'user1')

	def test_TickerForm_is_valid(self):
		form = TickerForm(data={'ticker':'FB'})
		self.assertTrue(form.is_valid())

	def test_CryptoTickerForm_is_valid(self):
		crypto_form = CryptoTickerForm(data={'crypto_ticker':'btcusd'})
		self.assertTrue(crypto_form.is_valid())




	

