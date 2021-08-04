from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Import CustomUser Model
from .models import CustomUser

# Define a form that creates a user in the datanbase when the user signsup
class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('username', 'email', 'subscribed')
		help_texts = {
			'username': None,
			
		}

# Form for updating user details
class CustomUserChangeForm(UserChangeForm):

	class Meta(UserChangeForm.Meta):
		model = CustomUser
		fields = ('username', 'email', 'subscribed')