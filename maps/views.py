from django.shortcuts import render, redirect
from maps.models import Pins, CheckIns
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.models import Integrations, IntegrationsUsers

import collections,json

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/users/login/')
def index(request):
	user = request.user
	checkins = CheckIns.objects.filter(user_id = user)

	all_data = []
	for checkin in checkins:
		checkin_data = {}

		checkin_data['title'] = checkin.pin.name
		checkin_data['lat'] = float(checkin.pin.latitude)
		checkin_data['lng'] = float(checkin.pin.longitude)
		checkin_data['address'] = checkin.pin.address
		checkin_data['city'] = checkin.pin.city
		checkin_data['state'] = checkin.pin.state
		checkin_data['country'] = checkin.pin.country
		checkin_data['business_url'] = checkin.pin.url
		checkin_data['date'] = str(checkin.date)
		checkin_data['integration_url'] = checkin.pin.integration.venue_url + checkin.pin.api_venue_id + "?ref=" + checkin.pin.integration.client_key

		all_data.append(checkin_data)

	json_data = json.dumps(all_data)
	
	return render(request,'maps/map_google.html',{"pin_data" : json_data})