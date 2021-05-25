from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
	subscribed = models.BooleanField(default=False)

	def __repr__(self):
		return self.username

	# def get_absolute_url(self):
	# 	return reverse('pages:userhome', kwargs={'username':self.username})
