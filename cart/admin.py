from django.contrib import admin
from .models import Cart, City, UserAddress
# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    
    class Meta:
    	model = Cart


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    
    class Meta:
    	model = City


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    
    class Meta:
    	model = UserAddress
