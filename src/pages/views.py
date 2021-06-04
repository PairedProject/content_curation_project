from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

from users.models import CustomUser
from stocks.models import Stocks
from .forms import TickerForm

# Create landing page
class HomePageView(TemplateView):
	template_name = 'home.html'


# Define user logged in page.
def index_view(request):

	# Create blank form instance
	form = TickerForm()
	
	# Check if theres data on the post request and if there is pass it to the Tickerform() instance
	if request.method == 'POST':
		post_data = request.POST or None
		if post_data != None:
			form = TickerForm(request.POST)
			# check if form is valid. 
			if form.is_valid():
				# If it is get the 'ticker' value from the form and store it the ticker variable
				ticker = form.cleaned_data.get('ticker')
				
				# If the variable ticker exists in the users portfolio send error message
				try: 
					if request.user.stocks_set.get(ticker=ticker) != None:
						messages.info(request, 'Stock ticker already exists in portfolio.')
				# Else create the Stock Object in the database and link it to the current user
				except Stocks.DoesNotExist:
					Stocks.objects.create(
						ticker = ticker, 
						user=request.user)

	# Call a list of the users stocks and store it to be passed into the context.
	stock_list = request.user.stocks_set.all()

	context = {
		'form' : form,
		'stock_list' : stock_list,
	}

	return render(request, 'index.html', context)

	


