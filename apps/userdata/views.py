''' userdata views '''
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from compat.decorators import render_to
from apps.userdata.models import Profile
from apps.userdata.forms import ProfileForm


@login_required
@render_to('profile_list.html')
def profile_list(request):
    ''' list profiles '''
    return {'profile_list': Profile.objects.all()}


@login_required
@render_to('profile_edit.html')
def profile_edit(request, pid):
    ''' edit profile '''
    profile = get_object_or_404(Profile, pk=pid)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=profile)
    return {'form': form}
