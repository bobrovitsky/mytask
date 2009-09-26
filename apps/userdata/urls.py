from django.conf.urls.defaults import *

urlpatterns = patterns('userdata.views',
	url(r'^$', 'profile_list'),
	url(r'^edit/(?P<pid>\d+)/$', 'profile_edit'),
)