''' allmodels command '''
from django.core.management.base import BaseCommand
from django.db.models.loading import get_models


class Command(BaseCommand):
    ''' call python manage.py allmodels '''

    def handle(self, *args, **options):
        ''' get all models and count objects '''
        models = get_models()
        for model in models:
            print model.__name__, ':', model.objects.count()
