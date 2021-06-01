from django.shortcuts import render
from users.models import CustomUser

from django.views.generic import DetailView

class StockDetailView(DetailView):
	
	template_name = 'stock_detail.html'

	def get_object(self, *args, **kwargs):
		request = self.request
		ticker = self.kwargs.get('ticker')
		instance = request.user.stocks_set.get(ticker=ticker)
		if instance is None:
			raise Http404('Stock does not exist')
		return instance

	def get_context_data(self, *args, **kwargs):
		request = self.request
		ticker = self.kwargs.get('ticker')
		context = super(StockDetailView, self).get_context_data(*args, **kwargs)
		instance = request.user.stocks_set.get(ticker=ticker)
		context['instance'] = instance
		return context
