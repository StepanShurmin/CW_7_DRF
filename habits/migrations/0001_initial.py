# Generated by Django 4.2.8 on 2023-12-05 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place", models.CharField(max_length=150, verbose_name="Место")),
                ("time", models.TimeField(verbose_name="Время ")),
                ("action", models.CharField(max_length=150, verbose_name="Действие")),
                (
                    "is_nice",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "periodicity",
                    models.PositiveIntegerField(
                        default=1,
                        verbose_name="Периодичность выполнения привычки в днях",
                    ),
                ),
                (
                    "reward",
                    models.CharField(max_length=150, verbose_name="Вознаграждение"),
                ),
                (
                    "execution_time",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Время на выполнение"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=True, verbose_name="Признак публичности"
                    ),
                ),
                (
                    "associated_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]