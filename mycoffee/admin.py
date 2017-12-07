from django.contrib import admin

# Register your models here.
from .models import Bean, Roast, Syrup, Powder, Coffee

@admin.register(Bean)
class BeanAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    class Meta:
    	model = Bean

@admin.register(Roast)
class RoastAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    class Meta:
    	model = Roast

@admin.register(Syrup)
class SyrpsAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    class Meta:
    	model = Syrup

@admin.register(Powder)
class PowderAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    class Meta:
    	model = Powder


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    class Meta:
    	model = Coffee

