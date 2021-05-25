from django.urls import path, include

from .views import HomePageView, index_view #home_page_view, home_page_user_view

app_name = 'pages'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('index/', index_view, name='index'),
    #path('<str:username>', home_page_user_view, name='userhome'),
]