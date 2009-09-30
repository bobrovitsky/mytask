''' modellog models '''
from django.db import models
from django.utils.translation import ugettext as _
from django.db.models.loading import get_models
from django.db.models.signals import post_save, post_delete
from apps.querylog.models import QueryLog

ACTIONS = (
    (1, _('create')),
    (2, _('update')),
    (3, _('remove')),
)


class ModelLog(models.Model):
    ''' model to store models actions '''
    model_name = models.CharField(_('model'), max_length=50)
    # why not int? because pk may be a string
    object = models.CharField(_('object'), max_length=255)
    action = models.IntegerField(_('action'), choices=ACTIONS)
    date = models.DateField(_('date'), auto_now=True)

    def __unicode__(self):
        ''' log description '''
        return (_('model=%s, object=%s, action=%s, date=%s'),
            self.model_name, self.object, self.action, self.date)

    def action_as_string(self):
        ''' return action as string instead of number '''
        return dict(ACTIONS).get(self.action)


def create_modellog(sender, instance, action):
    ''' create new modellog record'''
    ModelLog.objects.create(
        model_name=sender.__name__,
        object = str(instance.pk)[:255],
        action=action)


def update_model(sender, instance, created, **kwargs):
    ''' call when receive post_save signal '''
    action = 1 if created else 2
    create_modellog(sender, instance, action)


def delete_model(sender, instance, **kwargs):
    ''' call when receive post_delete signal '''
    create_modellog(sender, instance, 2)


for model in get_models():
    if model not in (QueryLog, ModelLog):
        post_save.connect(update_model, sender=model)
        post_delete.connect(delete_model, sender=model)
