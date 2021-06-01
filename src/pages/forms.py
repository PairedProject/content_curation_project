from django import forms
from stocks.models import Stocks

class TickerForm(forms.Form):
	ticker = forms.CharField(label='Ticker ', max_length=10)