''' userdata urls '''
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('userdata.views',
    url(r'^$', 'profile_list', name='profile_list'),
    url(r'^edit/(?P<pid>\d+)/$', 'profile_edit', name='profile_edit'),
)
