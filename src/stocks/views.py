from django.shortcuts import render, redirect
from users.models import CustomUser
from .models import Stocks
from django.views.generic import DetailView

# Define detail CBV to display stock meta and price data
class StockDetailView(DetailView):	
	template_name = 'stock_detail.html'

	# Define get_object() method for getting stock instance
	def get_object(self, *args, **kwargs):
		request = self.request
		ticker = self.kwargs.get('ticker')
		instance = request.user.stocks_set.get(ticker=ticker)
		if instance is None:
			raise Http404('Stock does not exist')
		return instance

	# Define method to pass context data to view
	def get_context_data(self, *args, **kwargs):
		request = self.request
		ticker = self.kwargs.get('ticker')
		context = super(StockDetailView, self).get_context_data(*args, **kwargs)
		instance = request.user.stocks_set.get(ticker=ticker)
		context['instance'] = instance
		return context


# Define a view for deleting a stock instance
def stock_delete_view(request, ticker):

	# Get the instance from the users portfolio
	stock = request.user.stocks_set.get(ticker=ticker)

	# Check if user clicked confirm, delete and redirect.
	if request.method == 'POST':
		stock.delete()
		return redirect('pages:index')

	context = {
		'stock' : stock,
	}

	return render(request, 'stock_delete.html', context)
