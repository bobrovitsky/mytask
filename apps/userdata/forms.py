from django import forms
from models import Profile
from widgets import DatePicker

class ProfileForm(forms.ModelForm):
	birthday = forms.DateField(required=True, widget=DatePicker)

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields.keyOrder.reverse()

	class Meta:
		model = Profile

