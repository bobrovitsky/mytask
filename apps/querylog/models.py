from django.db import models
from django.utils.translation import ugettext as _

class Log(models.Model):
	sql = models.TextField(_('query'))
	time = models.FloatField(_('time'))
	
	def __unicode__(self):
		return (_('query'))