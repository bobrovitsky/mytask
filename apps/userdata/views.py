from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from decorators import render_to
from models import Profile
from forms import ProfileForm

@login_required
@render_to('profile_list.html')
def profile_list(request):
	return {
		'profile_list': Profile.objects.all()
	}
	
@login_required
@render_to('profile_edit.html')
def profile_edit(request, pid):
	profile = get_object_or_404(Profile, pk=pid)
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save(commit=True)
	else:
		form = ProfileForm(instance=profile)
		print form.fields.keys()
	return {
		'form': form
	}