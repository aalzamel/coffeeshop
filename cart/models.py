from django.db import models
from mycoffee.models import Coffee
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, post_delete
from decimal import Decimal


class CartItem(models.Model):
	cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
	item = models.ForeignKey(Coffee, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	line_item_total = models.DecimalField(decimal_places = 3, max_digits = 20)
	
	def __str__(self):
		return self.item.name

def cart_item_pre_save(instance, *args, **kwargs):
	qty = instance.quantity
	if int(qty) >= 1 :
		price = instance.item.price
		total = price * Decimal(qty)
		instance.line_item_total = total
		# instance.cart.calc_subtotal()


pre_save.connect(cart_item_pre_save, sender=CartItem)


def cart_item_receiver(instance, *args, **kwargs):
	instance.cart.calc_subtotal()

post_save.connect(cart_item_receiver, sender=CartItem)
post_delete.connect(cart_item_receiver, sender=CartItem)


class Cart(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
	items = models.ManyToManyField(Coffee, through=CartItem)
	subtotal = models.DecimalField(decimal_places = 3, max_digits = 50, default=0.000)
	delivery_total = models.DecimalField(decimal_places = 3, max_digits = 50, default=2.000)
	total = models.DecimalField(decimal_places = 3, max_digits = 50, default=0.000)
	active = models.BooleanField(default=True)


	def __str__(self):
		return str(self.id)

	def calc_subtotal(self):
		sub = Decimal(0)
		items = self.cartitem_set.all()

		for item in items:
			sub += item.line_item_total
			self.subtotal = sub
			self.save()

def calc_delivery_total_and_total(instance, *args, **kwargs):
	instance.total = Decimal(instance.subtotal) + Decimal(instance.delivery_total)


pre_save.connect(calc_delivery_total_and_total, sender=Cart)





class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    block = models.CharField(max_length=3)
    avenue = models.PositiveIntegerField(blank=True, null=True)
    street = models.CharField(max_length=255)
    building_number = models.PositiveIntegerField()
    floor = models.CharField(max_length=3, null=True, blank=True)
    apt_number = models.PositiveIntegerField(null=True, blank=True)
    extra_directions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    address = models.ForeignKey(UserAddress, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.email)