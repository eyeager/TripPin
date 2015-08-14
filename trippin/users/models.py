from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Integrations(models.Model):
	name = models.CharField(max_length=30)
	client_key = models.CharField(max_length = 128)
	client_secret = models.CharField(max_length = 128)
	setup_url = models.CharField(max_length=384)
	data_url = models.CharField(max_length=384)

class IntegrationsUsers(models.Model):
	user_id = models.ForeignKey(User)
	integration_id = models.ForeignKey(Integrations)
	auth_key = models.CharField(max_length = 128)
	is_active = models.BooleanField()