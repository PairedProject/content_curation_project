from django import forms
from stocks.models import Stocks

"""

Forms for capturing users input.

"""
class TickerForm(forms.Form):
	ticker = forms.CharField(label='Ticker ', max_length=10)

class CryptoTickerForm(forms.Form):
	crypto_ticker = forms.CharField(label='Crypto Ticker', max_length=10)