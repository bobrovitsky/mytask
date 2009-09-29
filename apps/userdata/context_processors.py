''' add contexts to templates '''
from django.conf import settings


def settings_context(request):
    ''' add settings to template context '''
    return {'settings': settings}


def user_context(request):
    ''' add request.user to template context '''
    return {'user': request.user}
