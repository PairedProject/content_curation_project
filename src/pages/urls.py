from django.urls import path, include

from .views import HomePageView, index_view
from stocks.views import StockDetailView

app_name = 'pages'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('index/', index_view, name='index'),
	path('index/<str:ticker>', StockDetailView.as_view(), name='stock-detail'),
]