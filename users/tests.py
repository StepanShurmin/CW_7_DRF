from django.core.management import call_command
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self):
        self.url = "/users/user/"
        self.data = {"email": "test@email.com", "password": "123"}

    def test_create_user(self):
        response = self.client.post(f"{self.url}", data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(User.objects.all()[0].email, "test@email.com")

    def test_csu_command(self):
        call_command("csu")
        user = User.objects.all()[0]
        self.assertEqual(user.email, "admin@email.com")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
