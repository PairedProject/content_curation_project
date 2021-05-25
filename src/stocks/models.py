from django.db import models
from users.models import CustomUser

class Stocks(models.Model):
	ticker = models.CharField(max_length=5)
	user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.ticker
