from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
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
			return redirect("/")
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
