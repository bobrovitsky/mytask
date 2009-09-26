from django.conf import settings

def settings(request):
	return {'settings':settings}
	
def user(request):
	return {'user':request.user}