from decorators import render_to
from models import Profile

@render_to('profile_list.html')
def profile_list(request):
	return {
		'profile_list': Profile.objects.all()
	}