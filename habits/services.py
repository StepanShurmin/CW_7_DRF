import os

import requests

from users.models import User

URL = os.getenv("URL")
TOKEN = os.getenv("TLG_TOKEN")


def send_message(text, chat_id):
    requests.post(url=f"{URL}{TOKEN}/sendMessage", data={"chat_id": chat_id, "text": text})


def get_updates():
    response = requests.get(f"{URL}{TOKEN}/getUpdates")
    return response.json()


def parse_updates(updates):
    for u in updates:
        user = User.objects.get(tlg_info=u["message"]["chat"]["username"])
        if User.objects.filter(tlg_info=user).exist():
            user.chat_id = u["message"]["chat"]["id"]
            user.update_id = u["update_id"]
            user.save()
