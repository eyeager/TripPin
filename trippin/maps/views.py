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
	checkins = CheckIns.objects.filter(user_id= user)

	targetSVG = "M16,3.5c-4.142,0-7.5,3.358-7.5,7.5c0,4.143,7.5,18.121,7.5,18.121S23.5,15.143,23.5,11C23.5,6.858,20.143,3.5,16,3.5z M16,14.584c-1.979,0-3.584-1.604-3.584-3.584S14.021,7.416,16,7.416S19.584,9.021,19.584,11S17.979,14.584,16,14.584z";

	all_data = []
	for checkin in checkins:
		checkin_data = collections.OrderedDict()

		checkin_data['title'] = checkin.pin.name
		checkin_data['latitude'] = str(checkin.pin.latitude)
		checkin_data['longitude'] = str(checkin.pin.longitude)
		checkin_data['zoomLevel'] = 60
		checkin_data['scale'] = 0.5
		checkin_data['svgPath'] = targetSVG
		checkin_data['description'] = checkin.pin.address + checkin.pin.city + checkin.pin.country + checkin.pin.url


		all_data.append(checkin_data)

	json_data = json.dumps(all_data)
	# return HttpResponse(json_data)
	return render(request,'maps/map_2.html',{"pin_data" : json_data})