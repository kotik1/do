from django.conf.urls import url, include
from . import views
from django.core.urlresolvers import reverse

urlpatterns = [
	url(r'^$', views.intro),
	url(r'^catologue/$', views.catologue),
	url(r'^sell/$', views.sell),
	url(r'^buy/$', views.buy),
	url(r'^event/(?P<event>[\w\ ]{0,50})/$', views.event, name='event'),
	# url(r'^authfb/(?P<first_name>[\w\ ]{0,50})/(?P<last_name>[\w\ ]{0,50})/(?P<fb_id>[0-9]+)/$', views.authfb),
	url(r'^authfb/$', views.authfb),
	url(r'^authsteptwo/$', views.auth_step_two),
    # url(r'^authfb/$', views.authfb),
	# url(r'^authfbfrompage/$', views.authfbfrompage),
	# url(r'^update_fb_picture_url/$', views.update_fb_picture_url),
	# url(r'^logout/$', views.logout),
 #    url(r'^register/$', views.register),
 #    url(r'^delete_answer/$', views.delete_answer),
 #    url(r'^recover_answer/$', views.recover_answer),
 #    url(r'^save_changes/$', views.save_changes),
 #    url(r'^loadmore/(?P<page_number>[0-9]+)/(?P<uid>[0-9]+)/$', views.loadmore),
 #    url(r'^like/$', views.like),
 #    url(r'^dislike/$', views.dislike),
 #    url(r'^notify/$', views.notify,name='notify'),
 #    url(r'^user/(?P<username>\w{0,50})/$', views.user, name='user'),
 #    url(r'^feed/$', views.feed),
 #    url(r'^follow/$', views.follow),
 #    url(r'^unfollow/$', views.unfollow),
 #    url(r'^questions/$', views.questions),
 #    url(r'^save_question/$', views.save_question),
 #    url(r'^save_answer/(?P<question_pk>[0-9]+)/$', views.save_answer),
 #    url(r'^$', views.fblogin),
]
