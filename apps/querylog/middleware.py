''' querylog middleware '''
from django.db import connection
from apps.querylog.models import Log


class QueryMiddleware(object):
    ''' middleware to catch all sql queries '''

    def process_view(self, request, func, args, kwargs):
        ''' call view, save queries and return response '''
        response = func(request, *args, **kwargs)
        for query in connection.queries[:]:
            Log.objects.create(sql=query['sql'], time=query['time'])
        return response
