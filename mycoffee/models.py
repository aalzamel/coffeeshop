from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bean(models.Model):
	name = models.CharField(max_length=120, blank=False, unique=True)
	price = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self.name

class Roast(models.Model):
	name = models.CharField(max_length=120, blank=False, unique=True)
	price = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self.name

class Syrup(models.Model):
	name = models.CharField(max_length=120, blank=False, unique=True)
	price = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self.name

class Powder(models.Model):
	name = models.CharField(max_length=120, blank=False, unique=True)
	price = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self.name


class Coffee(models.Model):

	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=120)
	espresso_shots = models.PositiveIntegerField(default=1)

	bean = models.ForeignKey(Bean, on_delete=models.SET_NULL, null=True)
	roast = models.ForeignKey(Roast, on_delete=models.SET_NULL, null=True)
	syrup = models.ManyToManyField(Syrup, blank=True)
	powder = models.ManyToManyField(Powder, blank=True)

	water = models.FloatField()
	steamed_milk = models.BooleanField(default=False)
	foam = models.BooleanField(default=True)
	extra_instructions = models.CharField(max_length=160, null=True, blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	favorite = models.BooleanField(default=False)

	def __str__(self):
		return self.name



