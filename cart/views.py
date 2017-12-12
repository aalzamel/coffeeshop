from django.shortcuts import render, redirect
from .models import Cart, CartItem, Order, UserAddress
from mycoffee.models import Coffee
from decimal import Decimal
from django.http import JsonResponse
from .forms import AddressForm, AddressSelectForm

# Create your views here.
def AddItem(request):
	if request.user.is_anonymous:
		return redirect("mycoffee:login")

	carts = Cart.objects.filter(user=request.user, active=True)
	if carts.exists():
		cart = carts.first()
	else:
		cart = Cart.objects.create(user=request.user)



	# cart, created = Cart.objects.get_or_create(user=request.user)

	item = request.GET.get('item_id')
	qty = request.GET.get('qty', 1)

	if item:
		coffee = Coffee.objects.get(id=item)
		cart_item, created = CartItem.objects.get_or_create(cart=cart, item=coffee)
		if int(qty) <= 0 :
			cart_item.delete()
		else:
			cart_item.quantity = int(qty)
			cart_item.save()

	# cart = Cart.objects.get(user=request.user)

	return render(request, 'cart.html', {'cart':cart})


# def cart_item_count(request):
# 	carts = Cart.objects.filter(user=request.user)
# 	if not carts.exists():
# 		cart = Cart.objects.create(user=request.user)
# 	else:
# 		cart = carts.last()
# 	number = cart.cartitems_set.count()

def recal_item(request):
	item_id = request.GET.get("item_id")
	pre_delete = item_id
	qty = request.GET.get("qty")
	item = CartItem.objects.get(id=item_id)
	status = ""
	item.quantity=qty
	if int(qty) <= 0:
		status="delete"
		item.delete()
	else:
		item.save()

	resp = {
		"id":item.id,
		"quantity": item.quantity,
		"total": item.line_item_total,
		"status":status,
		"pre_delete":pre_delete,
	}

	return JsonResponse(resp, safe=False)


def recal_total(request):
	cart_id = request.GET.get("cart_id")
	current_cart = Cart.objects.get(id=cart_id)
	total = current_cart.total
	subtotal = current_cart.subtotal

	context = {
		'cart_id': cart_id,
		'subtotal': subtotal,
		'total': total,
	}
	return JsonResponse(context, safe=False)






############### Check out views



def checkout(request):
	# cart = Cart.objects.filter(user=request.user, active=True)
	# cart, created = Cart.objects.get_or_create(user=request.user)
	carts = Cart.objects.filter(user=request.user, active=True)
	if carts.exists():
		cart = carts.first()
	else:
		cart = Cart.objects.create(user=request.user)
	order, created = Order.objects.get_or_create(cart=cart, user=request.user)

	if order.address == None:
		return redirect("cart:select_address")
	return redirect("payment:checkout", order_id=order.id) 

def select_address(request):
	if UserAddress.objects.filter(user=request.user).count()<1:
		return redirect("cart:create_address")
	form = AddressSelectForm()
	form.fields['address'].queryset = UserAddress.objects.filter(user=request.user)
	if request.method == 'POST':
		form = AddressSelectForm(request.POST)
		if form.is_valid():
			address = form.cleaned_data['address']
			cart = Cart.objects.get(user=request.user, active=True)
			order = Order.objects.get(user=request.user, cart=cart)
			order.address=address
			order.save()
			return redirect("cart:checkout")
	context = {
		'form':form
	}
	return render(request, 'select_address.html', context)

def create_address(request):
	form = AddressForm()
	if request.method == 'POST':
		form = AddressForm(request.POST)
		if form.is_valid():
			address =form.save(commit=False)
			address.user = request.user
			address.save()
			form.save()
			return redirect("cart:select_address")
	context = {
		"form": form
	}
	return render(request, 'create_address.html', context)