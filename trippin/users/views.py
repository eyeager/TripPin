from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import requests

from django.http import HttpResponse

# Create your views here.

@login_required(login_url='/users/login/')
def index(request):
	return render(request, 'trippin/error.html',{"error_message": "I'm the INDEX"})

def signup(request):
	return render(request, 'users/signup.html',{})

def register(request):
	user = User.objects.create_user(first_name = request.POST["first_name"], last_name = request.POST["last_name"], username = request.POST["username"], email = request.POST["email"], password = request.POST["password"])

	return redirect('/users/login/')

def login_page(request):
	return render(request, 'users/login.html',{})

def login_user(request):
	user = authenticate(username=request.POST["username"], password=request.POST["password"])
	if user is not None:
	    # the password verified for the user
	    if user.is_active:
	    	login(request,user)
	    	next = request.POST["next"]
	    	if not next:
	    		next = '/users/profile'
	    	return redirect(next)
	    else:
	    	# Account exists, but is disabled
	    	return render(request, 'trippin/error.html',{"error_message": "The password is valid, but the account has been disabled!"})
	else:
	    # the authentication system was unable to verify the username and password
	    return render(request, 'trippin/error.html',{"error_message": "The username and password were incorrect."})

def logout_user(request):
	logout(request)
	return redirect('/users')

@login_required(login_url='/users/login/')
def profile(request):
	request_context = RequestContext(request)

	return render(request, 'users/profile.html',request_context)

@login_required(login_url='/users/login/')
def edit_profile(request):
	return render(request, 'users/edit_profile.html', {})

@login_required(login_url='/users/login/')
def save_profile(request):
	user = request.user
	something = request.POST.items()

	for data in request.POST.items():
		if data[1]:
			setattr(user, data[0], data[1])
			user.save()

	return redirect('/users/profile')

@login_required(login_url='/users/login/')
def change_password(request):
	return render(request, 'users/change_password.html', {})

@login_required(login_url='/users/login/')
def save_password(request):
	new_pass = request.POST["password"]
	return HttpResponse(new_pass)

@login_required(login_url='/users/login/')
def setup_api(request):
	api_code = request.GET.get('code')

	# Change this URL to be made from URL saved in DB
	api_setup_url = "https://foursquare.com/oauth2/access_token?client_id=204PWYPMJ2UTC4MGHTRQTAJUKUGN0VKCGNFOVKOWB3QPUFO1&client_secret=DVQGPNPU0SKJMBB5MWBYIOJBOQX00QYBEIU2KIFSRDBWWFQA&grant_type=authorization_code&redirect_uri=http://patchworkaustin.com/&code=" + api_code

	json_data = requests.get(api_setup_url).json()

	return HttpResponse(json_data["access_token"])
