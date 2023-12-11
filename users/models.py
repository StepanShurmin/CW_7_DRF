from django.contrib.auth.models import AbstractUser
from django.db import models

from habits.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    tlg_number = models.CharField(unique=True, verbose_name="Номер а телеге", **NULLABLE)
    name = models.CharField(max_length=50, verbose_name="Имя", **NULLABLE)
    chat_id = models.PositiveIntegerField(default=0, verbose_name="Номер чата", **NULLABLE)
    update_id = models.PositiveIntegerField(default=0, verbose_name="Номер последнего сообщения", **NULLABLE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
