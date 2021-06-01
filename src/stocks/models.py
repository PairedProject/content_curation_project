from django.db import models
from users.models import CustomUser
from django.urls import reverse

class Stocks(models.Model):
	ticker = models.CharField(max_length=5)
	user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.ticker

	def get_absolute_url(self):
		return reverse('pages:stock-detail', kwargs={'ticker': self.ticker})
