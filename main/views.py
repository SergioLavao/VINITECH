from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
	return render(request, 'index.html')	

def login(request):

	if request.POST:
		
		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(request, username=username, password=password)

		if user is not None:
			auth_login(request, user)
			print('Bienvenido')
			return redirect('/')
		else:
			return HttpResponse("Usuario invalido.")

	else:

		return render(request, 'login.html')

def register(request):

	if request.POST:

		username = request.POST["username"]
		password = request.POST["password"]

	

	else:

		return render(request, 'register.html')