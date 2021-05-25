from django import forms
from stocks.models import Stocks

# class TickerForm(forms.ModelForm):
# 	class Meta:
# 		model = Stocks
# 		fields = ['ticker']

class TickerForm(forms.Form):
	ticker = forms.CharField(label='Ticker ', max_length=10)