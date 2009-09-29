''' modellog views '''
from django.contrib.auth.decorators import login_required
from compat.decorators import render_to
from models import ModelLog


@login_required
@render_to('modellog_list.html')
def modellog_list(request):
    ''' show all records in modellog '''
    return {'modellog_list': ModelLog.objects.all()}
