from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages

from users.models import CustomUser
from stocks.models import Stocks
from .forms import TickerForm

class HomePageView(TemplateView):
	template_name = 'home.html'


def index_view(request):
	form = TickerForm()
	
	if request.method == 'POST':
		post_data = request.POST or None
		if post_data != None:
			form = TickerForm(request.POST)
			# print(form.is_valid())
			if form.is_valid():
				ticker = form.cleaned_data.get('ticker')
				try: 
					if request.user.stocks_set.get(ticker=ticker) != None:
						messages.info(request, 'Stock ticker already exists in portfolio.')
					
				except Stocks.DoesNotExist:
					Stocks.objects.create(
						ticker = ticker, 
						user=request.user)
					

	context = {
		'form' : form
	}

	return render(request, 'index.html', context)

	


