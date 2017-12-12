from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [

	path('checkout/<int:order_id>/', views.pay, name='checkout'),
	path('unsuccessful_payment/', views.unsuccessful_payment, name='unsuccessful_payment'),
	path('successful_payment/', views.successful_payment, name='successful_payment'),

]
