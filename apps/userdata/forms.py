''' forms definition  '''
from django import forms
from apps.userdata.models import Profile
from apps.userdata.widgets import DatePicker


class ProfileForm(forms.ModelForm):
    ''' profile form with custum DatePicker widget '''

    birthday = forms.DateField(required=True, widget=DatePicker)

    def __init__(self, *args, **kwargs):
        ''' redefine init method to change fields order '''
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder.reverse()

    class Meta:
        ''' make form from model Profile '''
        model = Profile
