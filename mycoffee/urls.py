from django.urls import path
from . import views

app_name = 'mycoffee'

urlpatterns = [

	path('signup/', views.UserSignUp, name='signup'),
	path('login/', views.UserLogin, name='login'),
	path('logout/', views.UserLogout, name='logout'),
	path('create_coffee/', views.CreateCoffee, name='CreateCoffee'),
	path('get_price/', views.get_price, name='get-price'),
]
