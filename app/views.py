from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response

from lxml import html
import requests
from django_cron import CronJobBase, Schedule

from django.core.paginator import Paginator
from .models import *

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import TicketForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

# from .forms import AuthForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@api_view(['POST', ])
def authfb(request):
    # print (request.data['fb_first_name'],request.data['fb_last_name'])
    # if request.method == 'POST':
    #     first_name = request.data['fb_first_name']
    #     last_name = request.data['fb_last_name']
    #     user, created = UserProfile.objects.get_or_create(first_name=first_name)
    #     if created is False:
    #         user.last_name = last_name
    #         user.save()
    #     else:
    #         user.last_name = last_name
    #         user.save()
    # else:
    #     return "666"
    require_more_data = True
    if request.method == 'POST':
        first_name = request.data['fb_first_name']
        last_name = request.data['fb_last_name']
        fb_username = request.data['fb_username']
        fb_id = int(request.data['fb_id'])
        fb_link = request.data['fb_link']
        username = fb_username.replace(' ', '')
        print(fb_link)
        print (type(fb_id))

        # print(username)
        password = '112358'
        user = auth.authenticate(username=username, password=password)
        # print(type(username))
        # print(type(password))
        if user is not None:
            auth.login(request, user)
            username = auth.get_user(request).username
            print ('logged in succesfully')
            # user1 = UserProfile.user.objects.get(username=username)
            # if (user1.userprofile.phone_number):
            #     print ("hello")
            # email = auth.get_user(request).UserProfile.email
            # if phone_number and email:
            #     require_more_data = False
        else:
            user = User.objects.create_user(username=username, password=password)
            userprofile = UserProfile.objects.create(user=user, first_name=first_name, last_name=last_name)
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            print (userprofile)
    else:
        print("WTF")
    return Response(request.data)

@api_view(['POST', ])
def auth_step_two(request):
    if request.method == 'POST':
        phone_number = request.data['phone_number']
        email = request.data['email']
        user = request.user.UserProfile
        user.email = email
        user.phone_number = phone_number
        user.save()
    else:
        print("WTF")
    return Response(request.data)


def intro(request):
	page = requests.get('https://karabas.com')
	tree = html.fromstring(page.content)
	titles = tree.xpath('//div[@class="hidden-info"]/p/text()')
	# images = tree.xpath('//div[@class="hidden-info"]/p/text()')
	images = tree.xpath('//div[@class="posters-middle"]/a/img/@src')
	# parsing = [{'title': title, 'image': image} for title, image in zip(titles, images)]
	parsing0 = Fugazi(titles[0],images[0])
	parsing1 = Fugazi(titles[1],images[1])
	parsing2 = Fugazi(titles[2],images[2])
	parsing3 = Fugazi(titles[3],images[3])
	parsing4 = Fugazi(titles[4],images[4])
	parsing5 = Fugazi(titles[5],images[5])
	# print parsing0.image()
	parsing = [ parsing0, parsing1, parsing2, parsing3, parsing4, parsing5]
	# for i in range(5):
	# 	i = Fugazi()
	# first_five = parsing[:5]
	# print(posters)
	# parsing = {}
	# for idx,title in enumerate(titles):
	# 	for poster in posters:
	# 		link = parsing[idx]
	# 		link['title'] = title
	# 		link['image'] = image
		# print(link['image'])
	return render(request, "blog/intro.html", {'parsing':parsing})


def catologue(request, page_number=1):
	events = Event.objects.all()
	events_number = Event.objects.all().count()
	current_page = Paginator(events,15)
	return render(request, "blog/catologue.html", {'events':current_page.page(page_number), 'events_number':events_number})

def event(request, event):
    event = Event.objects.get(id=event)
    similar_events = Event.objects.filter(hashtag=event.hashtag)[:5]
    return render(request, "blog/event.html", {'event':event,'similar_events':similar_events})


def login(request):
    pass

def logout(request):
    pass


def sell(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TicketForm()
        return render(request, "blog/sell.html", {
        'form': form
    })
    # return render(request, "blog/sell.html")

def buy(request):
    pass

class Fugazi:
	def __init__(self, title, image):
		self.title = title 
		self.image = image


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'app.my_cron_job'    # a unique code

    def do(self):
        page = requests.get('https://karabas.com')
        tree = html.fromstring(page.content)
        links = tree.xpath('//div[@class="posters-middle"]/a/@href')
        titles = tree.xpath('//div[@class="hidden-info"]/p/text()')
        images = tree.xpath('//div[@class="posters-middle"]/a/img/@src')
        cities = tree.xpath('//div[@class="details"]/strong[@class="city"]/text()')
        places = tree.xpath('//div[@class="details"]/span[@class="place"]/text()')
        dates = tree.xpath('//div[@class="details"]/span[@class="date"]/text()')
        for link in links:
           event_page = requests.get(link)
           tree_event_page = html.fromstring(event_page.content)
           title = tree_event_page.xpath('//div[@class="max-wrap"]/div[@class="main-details"]/h1/text()')
           if title:
               image = tree_event_page.xpath('//div[@class="max-wrap"]/figure[@class="photo"]/img/@src')
               if len(image) == 0:
                   image = tree_event_page.xpath('//div[@class="max-wrap"]/figure[@class="photo"]/a/img/@src')
               place = tree_event_page.xpath('//a[@class="hallIframe"]/text()')
               city_date_time = tree_event_page.xpath('//span[@class="place"]/strong/text()')
               city_date_time_str = city_date_time[0]
               city, date_unformat, time_unformat = city_date_time_str.split(",")
               hashtag = tree_event_page.xpath('//span[@class="category"]/text()')
               description =  tree_event_page.xpath('//div[@class="about-event"]/div[@class="max-wrap"]/div[@class="text"]/p/text()')
               del description[0]
               description = ''.join(map(str, description))
               hashtag = ''.join(map(str, hashtag))
               # print(hashtag, description)
               event, created = Event.objects.get_or_create(title=title[0])
               if created is False:
                   event.image_link = image[0]
                   event.city = city
                   event.place = place[0]
                   event.date = date_unformat
                   event.hashtag = hashtag
                   event.description = description
                   event.save()
                   print (Event.objects.all().count())	

               else:
                   event.title = title[0]
                   event.image_link = image[0]
                   event.city = city
                   event.place = place[0]
                   event.date = date_unformat
                   event.hashtag = hashtag
                   event.description = description
                   event.save()
                   print (Event.objects.all().count())	







       