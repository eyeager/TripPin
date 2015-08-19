from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from time import strftime
from datetime import datetime
from django.template import RequestContext
from users.models import Integrations, IntegrationsUsers
from maps.models import Pins, CheckIns
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
	user = request.user
	api_code = request.GET.get('code')
	api_info = Integrations.objects.get(name=request.GET.get('api_type'))

	json_data = requests.get(api_info.setup_url + api_code).json()
	integration_user = IntegrationsUsers.objects.create(user_id=user, integration_id=api_info, auth_key=json_data["access_token"], is_active=True )

	return redirect('/users/profile/')

@login_required(login_url='/users/login/')
def import_api(request):
	user = request.user
	api_info = Integrations.objects.get(name=request.GET.get('api_type'))
	integration_user = IntegrationsUsers.objects.get(user_id=user)

	json_data = requests.get(api_info.data_url + integration_user.auth_key).json()

	# Ensures a valid json response
	# This json loop imports for foursquare/swarm
	if json_data["meta"]["code"] == 200:
		for each in json_data["response"]["checkins"]["items"]:

		# See if checkin(api_check_in_id) has already been imported
			if not CheckIns.objects.filter(api_check_in_id=each["id"]):
				# Check to see if api_venue_id and integration_id combo already exist
				if not Pins.objects.filter(api_venue_id=each["venue"]["id"],integration_id=api_info):

					city, address, url = "","",""
					# Ensuring that city, url, and formattedAddress are being used
					if "city" in each["venue"]["location"]:
						city = each["venue"]["location"]["city"]
					if "state" in each["venue"]["location"]:
						state = each["venue"]["location"]["state"]
					if "address" in each["venue"]["location"]:
						address = each["venue"]["location"]["address"]
					if "url" in each["venue"]["location"]:
						url = each["venue"]["location"]["url"]

				# 	Adding a pin
					pin_info = Pins.objects.create(api_venue_id=each["venue"]["id"],integration=api_info, name = each["venue"]["name"], latitude = each["venue"]["location"]["lat"], longitude = each["venue"]["location"]["lng"], address = address, city = city, state = state, country = each["venue"]["location"]["country"], url = url)

				# Else getting existing pin
				else:
					pin_info = Pins.objects.get(api_venue_id=each["venue"]["id"],integration_id=api_info)
				
				# Adding a checkin linking to pin				
				checkin_date = datetime.fromtimestamp(int(each["createdAt"])).strftime('%Y-%m-%d')
				check_in = CheckIns.objects.create(user=user, pin=pin_info, api_check_in_id=each["id"], date=checkin_date)

	else:
	    return render(request, 'trippin/error.html',{"error_message" : "ERROR: could not import data from %s" % api_info.name})

	return render(request, 'trippin/error.html',{"error_message" : "SUCCESS: imported data from %s" % api_info.name})
