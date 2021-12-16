from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from ...models import BaranUser


class Command(BaseCommand):
    help = "Create initial demo user for application"
    DRY_RUN = False

    def handle(self, *args, **options):
        with transaction.atomic():
            self.create_initial_user()

            if self.DRY_RUN:
                raise CommandError('DRY RUN')

    def create_initial_user(self):
        try:
            BaranUser.objects.get(username='baran')
        except ObjectDoesNotExist:
            user = BaranUser.objects.create_superuser('baran')
            user.set_password('qwerty')
            user.save()
