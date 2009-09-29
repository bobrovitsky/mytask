''' userdata widgets '''
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe
from django.template import Context, loader


class DatePicker(TextInput):
    ''' DatePicker widget '''

    template_name = 'date_picker.html'
    type = 'text'

    class Media:
        ''' define js and css '''
        css = {'all': ('/static/datePicker.css', ), }
        js = ('/static/date.js', '/static/jquery.datePicker.js', )

    def render_template(self, name, text):
        ''' render full widget template '''
        template = loader.get_template(self.template_name)
        context = {'name': name, 'input': text}
        return mark_safe(template.render(Context(context)))

    def render(self, name, value, attrs=None):
        ''' render DatePicker widget '''
        text = super(DatePicker, self).render(name, value, attrs)
        return self.render_template(name, text)
