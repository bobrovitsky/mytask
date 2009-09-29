''' querylog models '''
from django.db import models
from django.utils.translation import ugettext as _


class Log(models.Model):
    ''' Log model '''

    sql = models.TextField(_('query'))
    time = models.FloatField(_('time'))
