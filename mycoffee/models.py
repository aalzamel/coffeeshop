from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bean(models.Model):
	name = models.CharField(max_length=120, blank=False, unique=True)
	price = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self

class Roast(models.Model):
	name = models.CharField(max_length=120, blank=False, unique=True)
	price = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self

class Syrups(models.Model):
	name = models.CharField(max_length=120, blank=False, unique=True)
	price = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self

class Powders(models.Model):
	name = models.CharField(max_length=120, blank=False, unique=True)
	price = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self


class Coffee(models.Model):

	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=120)
	espresso_shots = models.PositiveIntegerField(default=1)

	bean = models.ForeignKey(Bean, on_delete=models.SET_NULL, null=True)
	roast = models.ForeignKey(Roast, on_delete=models.SET_NULL, null=True)
	syrups = models.ManyToManyField(Syrups, blank=True)
	powders = models.ManyToManyField(Powders, blank=True)

	water = models.FloatField()
	steamed_milk = models.BooleanField(default=False)
	foam = models.BooleanField()
	extra_instructions = models.CharField(max_length=160, null=True, blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	def __str__(self):
		return self



