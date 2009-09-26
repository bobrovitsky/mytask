from django.forms import ModelForm
from models import Profile

class ProfileForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields.keyOrder.reverse()

	class Meta:
		model = Profile

