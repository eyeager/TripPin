from django.db import models
from django.contrib.auth.models import User
from users.models import Integrations

# Create your models here.

class Pins(models.Model):
	api_venue_id = models.CharField(max_length=50)
	integration_id = models.ForeignKey(Integrations)
	name = models.CharField(max_length=50)
	longitude = models.DecimalField(max_digits=15, decimal_places=14)
	latitude = models.DecimalField(max_digits=15, decimal_places=14)
	address = models.CharField(max_length=150)
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	url = models.CharField(max_length=100)

class CheckIns(models.Model):
	user_id = models.ForeignKey(User)
	pin_id = models.ForeignKey(Pins)
	# map_id = 
	api_check_in_id = models.CharField(max_length=50)
	date = models.DateField()

# class maps(models.Model):
# 	map_url = 