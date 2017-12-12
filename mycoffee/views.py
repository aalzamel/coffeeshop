from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserLoginForm, CoffeeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from decimal import Decimal
from .models import Coffee, Roast, Bean, Powder, Syrup
from django.http import JsonResponse
import json





def CoffeePrice(instance):
	total_price = instance.bean.price + instance.roast.price + (instance.espresso_shots*Decimal(0.500))
	if instance.steamed_milk:
		total_price+= Decimal(0.100)
	if instance.powder.all().count()>0:
		for powder in instance.powder.all():
			total_price+= powder.price
	if instance.syrup.all().count()>0:
		for syrup in instance.syrup.all():
			total_price+= syrup.price
	return total_price

def CreateCoffee(request):

	if not request.user.is_authenticated:
		return redirect("mycoffee:login")


	form = CoffeeForm()
	if request.method == "POST":
		form = CoffeeForm(request.POST)
		if form.is_valid():
			coffee = form.save(commit=False)
			coffee.user = request.user
			coffee.save()
			form.save_m2m()
			coffee.price = CoffeePrice(coffee)
			coffee.save()
			return redirect("/add?item_id=%s&qty=%s" % (coffee.id, 1))
			# return redirect('mycoffee:CreateCoffee')

	if request.user.is_authenticated:
		menu = Coffee.objects.filter(user__is_staff=True)
		favorites = Coffee.objects.filter(user=request.user, favorite=True)


	context = {
		'menu': menu,
		'favorites': favorites,

	}
	# context = {
	# 	'menu': menu,
	# 	'favorites': favorites,
	# 	'form': form,
	# }

	context['form'] = form



	return render(request, 'create_coffee.html', context)


	# if request.user.is_authenticated:
# 	favorite = Coffee.objects.filter(user=request.user, favorite=True)
# 	menu = Coffee.objects.filter(user__is_staff=True)


############# view to get price for axaj


def get_price(request):

	total_price = Decimal(0)
	bean_id = request.GET.get("bean")
	if bean_id:
		total_price += Bean.objects.get(id=bean_id).price	

	roast_id = request.GET.get("roast")
	if roast_id:
		total_price += Roast.objects.get(id=roast_id).price

	syrup = json.loads(request.GET.get("syrup"))
	for syrup_id in syrup:
		total_price += Syrup.objects.get(id=syrup_id).price

	powder = json.loads(request.GET.get("powder"))
	for powder_id in powder:
		total_price += Powder.objects.get(id=powder_id).price

	milk = request.GET.get("milk")
	if milk == 'true':
		total_price += Decimal(0.100)

	shots = request.GET.get("shots")
	total_price += Decimal(int(shots)*0.500)

	return JsonResponse(round(total_price,3), safe=False)

############# Athentication Views 


def UserSignUp(request):
	context = {}
	form = UserSignupForm()
	context['form'] = form
	if request.method == "POST":
		form = UserSignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = user.username
			password = user.password

			user.set_password(password)
			user.save()

			auth = authenticate(username=username, password=password)
			login(request, auth)
			return redirect("mycoffee:CreateCoffee")
		messages.warning(request, form.errors)
		return redirect('mycoffee:signup')
	return render(request, "usersignup.html", context)

def UserLogin(request):
	context = {}
	form = UserLoginForm()
	context['form'] = form

	if request.method == "POST":
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			auth = authenticate(username=username, password=password)
			if auth is not None:
				login(request, auth)
				return redirect("/")
			messages.warning(request, "Incorrect username/password combination")	
			return redirect('mycoffee:login')
		messages.warning(request, form.errors)
		return redirect('mycoffee:login')
	return render(request, "login.html", context)

def UserLogout(request):
	messages.success(request, "successfully logged out")
	logout(request)
	return redirect("/")


# 