
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe
from django.template import Context, loader

class DatePicker(TextInput):
	template = 'date_picker.html'
	type = 'text'

	class Media:
		css = {'all': ('/static/datePicker.css', ), }
		js = ('/static/date.js', '/static/jquery.datePicker.js', )
 
	def render(self, name, value, attrs=None):
		input = super(DatePicker, self).render(name, value, attrs)
		print input
		t = loader.get_template(self.template)
		c = {'name': name, 'input': input}			
		html = t.render(Context(c))
		return mark_safe(html)