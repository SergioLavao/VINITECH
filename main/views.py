from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse

@login_required(login_url='/login/')
def index(request):
	user_data = { 'username' : request.user.username }
	return render(request, 'index.html', user_data)	

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
			return render(request, 'login.html', { 'error' : True })

	else:

		return render(request, 'login.html')

def register(request):

	template = 'register.html'


	if request.method == 'POST':

		try:

			valid_user = User.objects.get(username=request.POST["username"])
			return render(request, 'register.html', { 'error' : True })

		except User.DoesNotExist:

			user = User.objects.create_user( request.POST['username'], request.POST['email'], request.POST['password'])
			user.save()
			auth_login(request, user)
			print('user created')	
			return redirect('/')

	else:

		return render(request, 'register.html')