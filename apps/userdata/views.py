from django.contrib.auth.decorators import login_required
from decorators import render_to
from models import Profile

@login_required
@render_to('profile_list.html')
def profile_list(request):
	return {
		'profile_list': Profile.objects.all()
	}