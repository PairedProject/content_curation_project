from django.urls import path, include

from .views import home_page_view, index_view
from stocks.views import stock_delete_view, stock_detail_view
from crypto.views import crypto_detail_view

app_name = 'pages'

urlpatterns = [
	path('', home_page_view, name='home'),
	path('index/', index_view, name='index'),
	path('index/<str:ticker>', stock_detail_view, name='stock-detail'),
	path('index/<str:ticker>/delete', stock_delete_view, name='stock-delete'),
	path('index/crypto/<str:crypto_ticker>', crypto_detail_view, name='crypto-detail'),
]