''' querylog views '''
from django.contrib.auth.decorators import login_required
from compat.decorators import render_to
from apps.querylog.models import QueryLog


@login_required
@render_to('query_list.html')
def query_list(request):
    ''' render sql list '''
    return {'query_list': QueryLog.objects.all()}
