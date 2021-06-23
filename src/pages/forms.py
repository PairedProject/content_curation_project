from django import forms
from stocks.models import Stocks

"""
TickerForm for capturing users requested stock ticker.
"""
class TickerForm(forms.Form):
	ticker = forms.CharField(label='Ticker ', max_length=10)