from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class SignupPageTests(TestCase):

	username = 'newuser'
	email = 'newuser@gmail.com'
	subscribed = True

	def test_sign_up_page_status_code(self):
		response = self.client.get('/users/signup/')
		self.assertEquals(response.status_code, 200)

	def test_view_url_by_name(self):
		response = self.client.get(reverse('signup'))
		self.assertEquals(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('signup'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'signup.html')

	def test_user_signup_form(self):
		new_user = get_user_model().objects.create_user(
			username = self.username, 
			email = self.email,
			subscribed = True
			)
		self.assertEquals(get_user_model().objects.all().count(), 1)
		self.assertEquals(get_user_model().objects.all()[0].username, self.username)
		self.assertEquals(get_user_model().objects.all()[0].email, self.email)
		self.assertEquals(get_user_model().objects.all()[0].subscribed, self.subscribed)



















