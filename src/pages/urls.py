from django.urls import path, include

from .views import HomePageView, index_view
from stocks.views import stock_delete_view, stock_detail_view

app_name = 'pages'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('index/', index_view, name='index'),
	path('index/<str:ticker>', stock_detail_view, name='stock-detail'),
	path('index/<str:ticker>/delete', stock_delete_view, name='stock-delete'),
]