from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsUser
from habits.serializers import HabitSerializer


class HabitCreateApiView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save(user=self.request.user)
        new_habit.user = self.request.user
        new_habit.save()


class HabitListApiView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsUser]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user).order_by("id")


class HabitPublicListApiView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(is_public=True).order_by("id")


class HabitDetailApiView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsUser]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateApiView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsUser]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDestroyApiView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsUser]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
