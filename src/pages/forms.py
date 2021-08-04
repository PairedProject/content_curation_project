from django import forms
from stocks.models import Stocks

"""

Forms for capturing users input.

"""
class TickerForm(forms.Form):
	ticker = forms.CharField(label='', max_length=10)

class CryptoTickerForm(forms.Form):
	crypto_ticker = forms.CharField(label="", max_length=10)