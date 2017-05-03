from django.conf.urls import url, include
from . import views
from django.core.urlresolvers import reverse

urlpatterns = [
	url(r'^$', views.intro),
	url(r'^catologue/$', views.catologue),
	url(r'^sell/$', views.sell),
	url(r'^buy/$', views.buy),
	url(r'^search/$', views.search),
	url(r'^event/(?P<event>[\w\ ]{0,50})/$', views.event, name='event'),
	url(r'^event_to_sell/(?P<selected_id>[\w\ ]{0,50})/$', views.event_to_sell),
	# url(r'^authfb/(?P<first_name>[\w\ ]{0,50})/(?P<last_name>[\w\ ]{0,50})/(?P<fb_id>[0-9]+)/$', views.authfb),
	url(r'^authfb/$', views.authfb),
	url(r'^authvk/$', views.authvk),
	url(r'^authsteptwo/$', views.auth_step_two),
	url(r'^upload_ticket/$', views.upload_ticket),
	url(r'^live_search/$', views.live_search),
	url(r'^load_more/$', views.load_more),
	url(r'^dialogs/$', views.dialogs),
	url(r'^load_dialog/$', views.load_dialog),
	url(r'^send_message/$', views.send_message),
	url(r'^logout/$', views.logout),
	url(r'^change_ticket_owner/$', views.change_ticket_owner),

]
