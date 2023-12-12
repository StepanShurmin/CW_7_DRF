from django.conf import settings
from django.db import models

NULLABLE = {"null": True, "blank": True}


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Пользователь"
    )
    place = models.CharField(max_length=150, **NULLABLE, verbose_name="Место")
    time = models.DateTimeField(verbose_name="Время")
    action = models.CharField(max_length=150, verbose_name="Действие")
    is_nice = models.BooleanField(default=False, verbose_name="Признак приятной привычки")
    associated_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="Связанная привычка", **NULLABLE
    )
    periodicity = models.SmallIntegerField(verbose_name="Периодичность выполнения привычки в днях")
    reward = models.CharField(max_length=150, verbose_name="Вознаграждение", **NULLABLE)
    execution_time = models.SmallIntegerField(verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=True, verbose_name="Признак публичности")

    def __str__(self):
        return f"я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
