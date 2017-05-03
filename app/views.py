from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response

from lxml import html
import requests
from django_cron import CronJobBase, Schedule

from django.core.paginator import Paginator
from .models import *

from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core import serializers

# from .forms import AuthForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
import json

import sys



# Create your views here.
@api_view(['POST', ])
def authfb(request):
    require_more_data = True
    if request.method == 'POST':
        first_name = request.data['fb_first_name']
        last_name = request.data['fb_last_name']
        fb_picture = request.data['fb_picture']
        fb_friends_number = request.data['fb_friends_number']
        fb_username = request.data['fb_username']
        fb_id = int(request.data['fb_id'])
        fb_link = request.data['fb_link']
        username = fb_username.replace(' ', '')

        # print(username)
        password = '112358'
        user = auth.authenticate(username=username, password=password)
        # print(type(username))
        # print(type(password))
        if user is not None:
            auth.login(request, user)
            username = auth.get_user(request).username
            print ('logged in succesfully')
            # if user.userprofile == None:
            #     print('he has userprofile')
            # else:
            #     print('he has not userprofile, lets create')
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
    # print (request.user.userprofile.email)
    request.user.userprofile.number_of_friends = fb_friends_number
    request.user.userprofile.picture_link = fb_picture
    request.user.userprofile.save()
    email = request.user.userprofile.email
    phone_number = request.user.userprofile.phone_number
    # s_email = serializers.serialize('json', email)
    # s_phone_number = serializers.serialize('json', phone_number)
    # print (email)
    # print (phone_number)
    # data = {
    # 'email': s_email,
    # 'phone_number': s_phone_number,
    # }
    data = {
    'email': email,
    'phone_number': phone_number,
    }
    return Response(data)
    # return Response(request.data)

@api_view(['POST', ])
def authvk(request):
    require_more_data = True
    if request.method == 'POST':
        first_name = request.data['vk_first_name']
        last_name = request.data['vk_last_name']
        vk_picture = request.data['vk_picture']
        vk_friends_number = request.data['vk_friends_number']
        username = first_name + last_name
        # UsernameAlreadyTaken = User.objects.get(vk_username)
        # while UsernameAlreadyTaken == True
        #      vk_username = vk_username + '6'
        #      UsernameAlreadyTaken = User.objects.get(vk_username)
        # print(vk_username)
        vk_id_str = request.data['vk_id']
        print(vk_id_str)
        vk_id = int(vk_id_str)
        print(vk_id)
        vk_link = request.data['vk_link']
        # username = fb_username.replace(' ', '')

        # print(username)
        password = '1112358'
        user = auth.authenticate(username=username, password=password)
        # print(type(username))
        # print(type(password))
        if user is not None:
            auth.login(request, user)
            username = auth.get_user(request).username
            print ('logged in succesfully')
            # if user.userprofile == None:
            #     print('he has userprofile')
            # else:
            #     print('he has not userprofile, lets create')
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
        print(sys.version)
        print('ok')
        phone_number = request.data['phone_number']
        print('1')
        email = request.data['email']
        print('2')
        user = request.user.userprofile
        print('3')
        user.email = email
        print('4')
        user.phone_number = phone_number
        print('5')
        user.save()
        print('6')
        print(sys.version)
    else:
        print("WTF")
    return Response(request.data)




@api_view(['POST', ])
def live_search(request):
    if request.method == 'POST':
        # key = str(request.data['key'],'utf-8')
        # key = request.data['key']
        # print (key)
        # print (key)
        # key = u'key'
        # result = Event.objects.filter(title__istartswith=key)
        # t = key.decode('iso-8859-1')
        # print(t)
        u = unicode("Привет, мир!", cp1251)
        result = Event.objects.filter(body_text__search=u)
        events = serializers.serialize('json', result)
        print (key)
        print (result)
    else:
        error = "Fuck"
        return error
    data = {
        'events': events,

    }
    return Response(data)


@api_view(['POST', ])
def load_more(request):
    if request.method == 'POST':
        page_number = request.data['page_number']
        events = Event.objects.all()
        paginator = Paginator(events,15)
        current_page = (paginator.page(page_number))
        s_events = serializers.serialize('json', current_page)
    else:
        error = "Fuck"
        return error
    data = {
        'events': s_events,

    }
    return Response(data)


@api_view(['POST', ])
def dialogs(request, page_number=1):
    if request.method == 'POST':
        # page_number = request.data['page_number']
        # dialogs = request.user.userprofile.Dialog
        # dialogs = Event.objects.all().filter(buyer=request.user.userprofile)
        # dialogs = Event.objects.all().filfter(Q(buyer=request.user.userprofile) | Q(sales=request.user.userprofile))
        # dialogs = Event.objects.filter(sales=request.user.userprofile)
        dialogs = Dialog.objects.all()
        tickets = []
        events = []
        parties = []
        for dialog in dialogs:
            tickets.append(dialog.ticket)
            events.append(dialog.ticket.event)
            parties.append(dialog.ticket.ownership)
        # paginator = Paginator(events,15)
        # current_page = (paginator.page(page_number))
        current_page = Paginator(dialogs,6)
        s_dialogs = serializers.serialize('json', current_page.page(page_number))
        s_tickets = serializers.serialize('json', tickets)
        s_events= serializers.serialize('json', events)
        s_parties =  serializers.serialize('json', parties)
    else:
        error = "Fuck"
        return error
    data = {
        'dialogs': s_dialogs,
        'tickets': s_tickets,
        'events':  s_events,
        'parties': s_parties,

    }
    return Response(data)


@api_view(['POST', ])
def load_dialog(request):
    if request.method == 'POST':
        party_id = request.data['party_id']
        ticket_id = request.data['ticket_id']
        party = UserProfile.objects.get(pk=party_id)
        ticket = Ticket.objects.get(pk=ticket_id)
        try:
            dialog = Dialog.objects.get(Q(sales=party) | Q(sales=request.user.userprofile))
        except Dialog.DoesNotExist:
            dialog = None
        if dialog:
            textbool = None
            if dialog.sales == request.user.userprofile:
                textbool = "show"
            messages = Message.objects.filter(dialog=dialog)
            s_messages = serializers.serialize('json', messages)
            s_textbool = json.dumps(textbool)
            data = {
               'messages': s_messages,
               'sales': s_textbool,
            }
        else:
            print('i')
            owner = ticket.ownership
            new_dialog = Dialog.objects.create(buyer=request.user.userprofile,sales=owner,ticket=ticket)
            textbool = None
            if new_dialog.sales == request.user.userprofile:
                textbool = "show"
            messages = Message.objects.filter(dialog=new_dialog)
            s_messages = serializers.serialize('json', messages)
            s_textbool = json.dumps(textbool)
            # data = {
            #    'messages': s_messages,
            #    'sales': s_textbool,
            # }
            # s_error = json.dumps('error')
            # data = {
            #     'error': s_error,
            # }
        print('ni')
        # # dialog = Dialog.objects.get(Q(sales=party) | Q(sales=request.user.userprofile))
        # try:
        #     dialog = Dialog.objects.get(Q(sales=party) | Q(sales=request.user.userprofile))
        # except Dialog.DoesNotExist:
        #     dialog = None
        # # dialog = Dialog.objects.get(sales=party)
        # # dialog = Dialog.objects.get_or_create(sales=party,buyer=request.user.userprofile,ticket=ticket)
        # print('ni2')
    else:
        error = "Fuck"
        return error
    data = {
               'messages': s_messages,
               'sales': s_textbool,
            }
    return Response(data)



@api_view(['POST', ])
def send_message(request):
    party_id = int(request.data['party_id'])
    message = request.data['message']
    to_user = UserProfile.objects.get(pk=party_id)
    print(to_user)
    option_one = Dialog.objects.get(buyer=request.user.userprofile, sales=to_user)
    option_two = Dialog.objects.get(buyer=to_user, sales=request.user.userprofile)
    # print(Dialog.objects.all())
    print("ddd")
    if option_one:
       Message.objects.create(text=message,dialog=option_one,from_user=request.user.userprofile,to_user=to_user)

    elif option_two:
       Message.objects.create(text=message,dialog=option_two,from_user=request.user.userprofile,to_user=to_user)

    else:
       Dialog.objects.create(buyer=request.user.userprofile,sales=party_id)
    return Response(request.data)


@api_view(['POST', ])
def change_ticket_owner(request):
    ticket_id = request.data['ticket_id']
    new_owner_id = request.data['new_owner_id']
    ticket = Ticket.objects.get(pk=ticket_id)
    new_owner = UserProfile.objects.get(pk=new_owner_id)
    ticket.ownership = new_owner
    ticket.save()
    # if ticket.ownership == new_owner_id:
    return Response(request.data)




def search(request):
    if request.method == 'POST':
        key = request.POST.get("key")
        print (type(key))
        if key is not None:
            result = Event.objects.filter(title__istartswith=key)
            events_number = result.count()
            return render(request, "blog/catologue.html", {'events':result, 'events_number':events_number,'key':key})
        else:
            return redirect('/catologue/')
        


# def upload_ticket(request):
#     if request.method == 'POST':
#         form = TicketForm(request.POST)
#         # if form.is_valid():
#             # ticket = form.save(commit=False)
#             # ticket.ownership = request.user.userprofile
#             # ticket.event = Event.objects.get(id=9)
#             # ticket.save()
#         form.save()
#         print (Ticket.objects.all())
#         # else:
#         #     print('form is not valid');
#     else:
#         print("WTF")
#     return render(request, "blog/aftersale.html",{})



def upload_ticket(request):
    if request.method == 'POST':
        print ('hh')
        number = request.POST.get('event_id')
        print (number)
        # number = int(number)
        price = request.POST.get('price')
        comment = request.POST.get('comment')
        print(number)
        print(type(number))
        filename = request.POST.get('pdf')
        file = request.FILES
        ticket = Ticket()
        ticket.event = Event.objects.get(id=number)
        ticket.price = price
        ticket.comment = comment 
        ticket.ownership = request.user.userprofile
        ticket.upload = file['pdf']
        ticket.save()
        print (file)
        print (Ticket.objects.all())
    else:
        print("WTF")
    return render(request, "blog/aftersale.html",{})



# @api_view(['POST', ])
# def upload_ticket(request):
#     if request.method == 'POST':
#         print('ok')
#     else:
#         print("WTF")
#     return render(request, "blog/intro.html",{})



def intro(request):
  events  = Event.objects.all().order_by("date")[:7]
  return render(request, "blog/intro.html", {'events':events})


def catologue(request, page_number=1):
    events = Event.objects.all().order_by("date")
    events_number = Event.objects.all().count()
    current_page = Paginator(events,15)
    return render(request, "blog/catologue.html", {'events':current_page.page(page_number), 'events_number':events_number})

def event(request, event):
    event = Event.objects.get(id=event)
    similar_events = Event.objects.filter(hashtag=event.hashtag)[:5]
    proposals = Ticket.objects.filter(event=event)
    # print(proposals)
    return render(request, "blog/event.html", {'event':event,'similar_events':similar_events,'proposals':proposals})


def login(request):
    pass

def logout(request):
    pass


def event_to_sell(request,selected_id):
     form = TicketForm()
     selected = Event.objects.get(id=selected_id)
     return render(request, "blog/sell.html", {'form': form, 'selected':selected })

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
               print(date_unformat)
               hashtag = tree_event_page.xpath('//span[@class="category"]/text()')
               description =  tree_event_page.xpath('//div[@class="about-event"]/div[@class="max-wrap"]/div[@class="text"]/p/text()')
               del description[0]
               print (hashtag)
               description = ''.join(map(str, description))
               hashtag = ''.join(map(str, hashtag))
               print (hashtag)
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





def logout(request):
  auth.logout(request)
  return redirect('/')

       