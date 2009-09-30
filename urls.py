from django.conf.urls.defaults import *
import settings    

urlpatterns = patterns('',
    url('^static/(?P<path>.*)$', 'django.views.static.serve', 
		{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

urlpatterns += patterns('',
	url(r'', include('userdata.urls')),
)

urlpatterns += patterns('',
	url(r'^querylog/$', 'querylog.views.query_list', name='querylog_list'),
	url(r'^modellog/$', 'modellog.views.modellog_list', name='modellog_list'),
)

urlpatterns += patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login', 
        {'template_name':'login.html'}, name='login'
	)
)

urlpatterns += patterns('',
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', 
        {'login_url':'/login/'}, name='logout',
	)
)