from django.core.management import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):

    def handle(self, *args, **options):
        Group.objects.get_or_create(name='سرپرست')
        Group.objects.get_or_create(name='مدیر')
