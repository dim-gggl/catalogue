from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key
from django.conf import settings


class Command(BaseCommand):
    help = "Generate a SECRET_KEY and displays it"

    def handle(self, *args, **kwargs):
        secret_key = get_random_secret_key()
        self.stdout.write(secret_key)
        # old_secret_key = settings.SECRET_KEY
        # fallbacks = settings.SECRET_KEY_FALLBACKS
        # fallbacks.append(old_secret_key)
