from django.contrib import admin

# Register your models here.
from .models import Bean, Roast, Syrups, Powders, Coffee

admin.site.register(Bean)
admin.site.register(Roast)
admin.site.register(Syrups)
admin.site.register(Powders)
admin.site.register(Coffee)