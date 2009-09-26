from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from decorators import render_to
from models import Log

@login_required
@render_to('query_list.html')
def query_list(request):
	return {
		'query_list': Log.objects.all()
	}