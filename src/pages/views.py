from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
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
				#print(form.cleaned_data.get('ticker'))
				Stocks.objects.create(
					ticker = form.cleaned_data.get('ticker'), 
					user=request.user)

	context = {
		'form' : form
	}

	return render(request, 'index.html', context)

	


# 	if request.user.is_authenticated:
# 		stock_list = user.stocks_set.all()
# # 	#query_set = Stocks.objects.all()

	# def get_context_data(self, **kwargs):
	# 	request = self.request
	# 	user = request.user
	# 	print(user)
	# 	context = super().get_context_data(**kwargs)
	# 	context['user'] = user
	# 	return context

# 	print(request.session)

# 	# def get_context_data(self, **kwargs):
#  #        # Call the base implementation first to get a context
#  #        context = super().get_context_data(**kwargs)
#  #        # Add in a QuerySet of all the books
#  #        context['stock_list'] = Stocks.objects.all()
#  #        return context

# def home_page_view(request):

# 	return render(request, 'home.html', {})

# def home_page_user_view(request, username):
# 	# print(request.session)
# 	# print(dir(request.session))
# 	# key = request.session.session_key
# 	# print(key)
# 	user = CustomUser.objects.get(username=username)
# 	request.session['username'] = 'unknown'
# 	#print(user.username)
# 	if request.user.is_authenticated:
# 		request.session['username'] = user.username
# 	print(request.session.get('username'))

# 	return render(request, 'user_home.html', {})