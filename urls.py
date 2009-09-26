﻿from django.conf.urls.defaults import *
import settings    

urlpatterns = patterns('',
    url('^static/(?P<path>.*)$', 'django.views.static.serve', 
		{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

urlpatterns += patterns('',
	url(r'', include('userdata.urls')),
)