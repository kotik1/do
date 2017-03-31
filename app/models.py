from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	sn_link = models.CharField(max_length=100)
	SN_OPTIONS  = (
    ('1', 'facebook'),
    ('2', 'vk'),
	)
	sn = models.CharField(choices=SN_OPTIONS, max_length=2)
	phone_number = models.IntegerField()

class Event(models.Model):
	title = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	place = models.CharField(max_length=100)
	date = models.CharField(max_length=100)
	description = models.CharField(max_length=8000)
	hashtag = models.CharField(max_length=100)
	image_link = models.CharField(max_length=2000, default='https://pp.userapi.com/c626925/v626925096/1a33f/JD7FoQDRqXY.jpg')

class Ticket(models.Model):
	upload = models.FileField(upload_to='/tickets/', default='https://pp.userapi.com/c626925/v626925096/1a33f/JD7FoQDRqXY.jpg')
	ownership = models.OneToOneField(UserProfile)
	event = models.OneToOneField(Event)
	approved = models.BooleanField(default=False)
	sold = models.BooleanField(default=False)
