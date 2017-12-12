from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [

	path('add/', views.AddItem, name='add'),
	path('cart_update/', views.recal_item, name='cart_update'),
	path('subtotal/', views.recal_total, name='subtotal'),
	path('create_address/', views.create_address, name='create_address'),
	path('select_address/', views.select_address, name='select_address'),
	path('checkout/', views.checkout, name='checkout'),
]
