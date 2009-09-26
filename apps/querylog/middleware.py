from django.db import connection
from models import Log

class QueryMiddleware(object):
	def process_view(self, request, func, args, kwargs):
		response = func(request, *args, **kwargs)
		for query in connection.queries[:]:
			Log.objects.create(sql=query['sql'], time=query['time'])
		return response