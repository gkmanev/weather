
from django.core.management.base import BaseCommand
from weather_data.utils import fill_history_data


class Command(BaseCommand):
    help = 'fetch'

    def handle(self, *args, **kwargs):
        fill_history_data()
        self.stdout.write(self.style.SUCCESS('Fetch data successfull'))