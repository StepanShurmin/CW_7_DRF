from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@email.com", is_staff=True, is_active=True, is_superuser=True)
        self.user.set_password("123")
        self.user.save()

        response = self.client.post("/users/token/", {"email": "test@email.com", "password": "123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        self.data = {
            "place": "Earth",
            "time": "2023-12-13 10:00",
            "action": "test habit",
            "execution_time": "100",
            "periodicity": "1",
        }

    def test_create_habit(self):
        response = self.client.post(reverse("habits:create_habit"), self.data)
        pk = Habit.objects.all().latest("pk").pk
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                "id": pk,
                "place": "Earth",
                "time": "2023-12-13T10:00:00+04:00",
                "action": "test habit",
                "is_nice": False,
                "periodicity": 1,
                "reward": None,
                "execution_time": 100,
                "is_public": False,
                "user": self.user.pk,
                "associated_habit": None,
            },
        )

    def test_list_habit(self):
        self.test_create_habit()
        response = self.client.get(reverse("habits:list_habit"))
        pk = Habit.objects.all().latest("pk").pk

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json()["results"],
            [
                {
                    "id": pk,
                    "place": "Earth",
                    "time": "2023-12-13T10:00:00+04:00",
                    "action": "test habit",
                    "is_nice": False,
                    "periodicity": 1,
                    "reward": None,
                    "execution_time": 100,
                    "is_public": False,
                    "user": self.user.pk,
                    "associated_habit": None,
                }
            ],
        )

    def test_list_public_habit(self):
        response = self.client.get(reverse("habits:public_habit"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()["results"], [])

    def test_detail_habit(self):
        self.test_create_habit()
        pk = Habit.objects.all().latest("pk").pk
        response = self.client.get(reverse("habits:detail_habit", kwargs={"pk": pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "id": pk,
                "place": "Earth",
                "time": "2023-12-13T10:00:00+04:00",
                "action": "test habit",
                "is_nice": False,
                "periodicity": 1,
                "reward": None,
                "execution_time": 100,
                "is_public": False,
                "user": self.user.pk,
                "associated_habit": None,
            },
        )

    def test_update_habit(self):
        self.test_create_habit()
        pk = Habit.objects.all().latest("pk").pk
        response = self.client.patch(reverse("habits:update_habit", kwargs={"pk": pk}), data={"periodicity": "1"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "id": pk,
                "place": "Earth",
                "time": "2023-12-13T10:00:00+04:00",
                "action": "test habit",
                "is_nice": False,
                "periodicity": 1,
                "reward": None,
                "execution_time": 100,
                "is_public": False,
                "user": self.user.pk,
                "associated_habit": None,
            },
        )

    def test_habit_destroy(self):
        self.test_create_habit()
        pk = Habit.objects.all().latest("pk").pk
        response = self.client.delete(reverse("habits:delete_habit", kwargs={"pk": pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_nonexistent_habit(self):
        response = self.client.patch(
            reverse("habits:update_habit", kwargs={"pk": 999}),
            data={"periodicity": "1"},
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_nonexistent_habit(self):
        response = self.client.delete(reverse("habits:delete_habit", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_validate_ExecutionPeriodicityValidator(self):
        self.test_create_habit()
        pk = Habit.objects.all().latest("pk").pk
        url = reverse("habits:update_habit", kwargs={"pk": pk})
        response = self.client.patch(url, data={"periodicity": "8"})
        self.assertEqual(
            response.json(),
            {"non_field_errors": ["Нельзя выполнять привычку реже, чем 1 раз в 7 дней."]},
        )

    def test_validate_ExecutionTimeValidator(self):
        self.test_create_habit()
        pk = Habit.objects.all().latest("pk").pk
        url = reverse("habits:update_habit", kwargs={"pk": pk})
        response = self.client.patch(url, data={"execution_time": "121"})

        self.assertEqual(
            response.json(),
            {"non_field_errors": ["Время выполнения должно быть не больше 120 секунд."]},
        )
