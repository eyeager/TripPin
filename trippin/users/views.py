from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.http import HttpResponse

# Create your views here.

def signup(request):
	return render(request, 'users/signup.html',{})

def register(request):
	first_name = request.POST["first_name"]
	last_name = request.POST["last_name"]
	username = request.POST["username"]
	email = request.POST["email"]
	password = request.POST["password"]

	user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password)

	return redirect('users/login/')

def login(request):
	return render(request, 'users/login.html',{})

def login_user(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(username=username, password=password)
	if user is not None:
	    # the password verified for the user
	    if user.is_active:
	        return HttpResponse("User is valid, active and authenticated")
	    else:
	    	return render(request, 'trippin/error.html',{"error_message": "The password is valid, but the account has been disabled!"})
	else:
	    # the authentication system was unable to verify the username and password
	    return render(request, 'trippin/error.html',{"error_message": "The username and password were incorrect."})
