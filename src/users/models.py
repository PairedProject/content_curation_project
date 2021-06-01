from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	subscribed = models.BooleanField(default=False)

	def __repr__(self):
		return self.username
