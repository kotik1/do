from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	sn_link = models.CharField(max_length=100)
	phone_number = models.IntegerField(blank=True)
	email = models.CharField(max_length=100, blank=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	sn_id = models.IntegerField(blank=False, default=0)

class Event(models.Model):
	title = models.CharField(max_length=1000)
	city = models.CharField(max_length=1000)
	place = models.CharField(max_length=1000)
	date = models.CharField(max_length=100)
	description = models.CharField(max_length=10000)
	hashtag = models.CharField(max_length=1000) 
	image_link = models.CharField(max_length=2000, default='https://pp.userapi.com/c626925/v626925096/1a33f/JD7FoQDRqXY.jpg')

class Ticket(models.Model):
	upload = models.FileField(upload_to='media/tickets/')
	ownership = models.ForeignKey(UserProfile)
	event = models.ForeignKey(Event)
	price = models.IntegerField(blank=False, default=0)
	comment = models.CharField(max_length=2000)
	approved = models.BooleanField(default=False)
	sold = models.BooleanField(default=False)
	TICKET_CHOICES = (
    ('DG', 'Digital'),
    ('RL', 'Real'),
    )  
	ticket_type = models.CharField(
        max_length=2,
        choices=TICKET_CHOICES,
        default='Digital',
    )

class Dialog(models.Model):
    buyer = models.ForeignKey(UserProfile, related_name='buyer_reverse')
    sales = models.ForeignKey(UserProfile, related_name='sales_reverse')
    ticket = models.ForeignKey(Ticket)
    date_of_start = models.DateField(blank=True)


class Message(models.Model):
	dialog = models.ForeignKey(Dialog, related_name='dialog_reverse')
	from_user = models.ForeignKey(UserProfile, related_name='from_user_reverse')
	to_user = models.ForeignKey(UserProfile, related_name='to_user_reverse')
	text = models.CharField(max_length=2000)

