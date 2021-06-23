from django.db import models
from django.contrib.auth.models import AbstractUser

"""
Custom user model inheriting from Django's AbstarctUser Class.
"""
class CustomUser(AbstractUser):

	""" Add subscribed field to the model. """
	subscribed = models.BooleanField(default=False)

	def __repr__(self):
		return self.username
