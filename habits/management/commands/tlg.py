import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from habits.services import send_message

load_dotenv()

CHAT_ID = os.getenv("CHAT_ID")


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_message("dxfcgvhbjnj", CHAT_ID)
