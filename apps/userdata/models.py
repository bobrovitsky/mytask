''' userdata models '''
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse


class Profile(models.Model):
    ''' Profile model '''

    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    address = models.CharField(_('address'), max_length=255)
    description = models.TextField(_('description'))
    birthday = models.DateField(_('birthday'))

    def __unicode__(self):
        ''' represent profile object when call uncide method '''
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        ''' return link to edit profile object '''
        return reverse('profile_edit', kwargs={'pid': self.pk})
