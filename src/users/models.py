from django.db import models
from django.contrib.auth.models import AbstractUser

# Create custom user model iheriting from Django's AbstarctUser Class
class CustomUser(AbstractUser):

	# Add out own subscribed field to the model
	subscribed = models.BooleanField(default=False)

	def __repr__(self):
		return self.username
