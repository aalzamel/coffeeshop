from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mycoffee'

urlpatterns = [

	path('signup/', views.UserSignUp, name='signup'),
	path('login/', views.UserLogin, name='login'),
	path('logout/', views.UserLogout, name='logout'),

]
