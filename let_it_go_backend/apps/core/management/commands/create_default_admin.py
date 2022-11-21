from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = "Create a default admin account"

    def handle(self, *args, **options):
        with transaction.atomic():
            user, created = User.objects.get_or_create(username="admin")
            if created:
                user.set_password("admin")

                user.is_staff = True
                user.is_superuser = True

                user.save()
                self.stdout.write("Successfully created a default admin account")
            else:
                self.stdout.write("Default admin account already exists")
