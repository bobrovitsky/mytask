from django.core.management.base import BaseCommand
from django.db.models.loading import get_models

class Command(BaseCommand):
	def handle(self, *args, **options):
		models = get_models()
		for model in models:
			print model.__name__, ':', model.objects.count()