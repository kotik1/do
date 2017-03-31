from django.shortcuts import render
from django.shortcuts import render_to_response
from lxml import html
import requests
from django_cron import CronJobBase, Schedule
from django.core.paginator import Paginator
from .models import *
from .forms import TicketForm

# Create your views here.
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
    RUN_EVERY_MINS = 0.1 # every 2 hours

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







       