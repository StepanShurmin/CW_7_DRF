from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitCreateApiView,
    HabitListApiView,
    HabitDetailApiView,
    HabitPublicListApiView,
    HabitUpdateApiView,
    HabitDestroyApiView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("create/", HabitCreateApiView.as_view(), name="create_habit"),
    path("list/", HabitListApiView.as_view(), name="list_habit"),
    path("list/<int:pk>/", HabitDetailApiView.as_view(), name="detail_habit"),
    path("public/", HabitPublicListApiView.as_view(), name="public_habit"),
    path("update/<int:pk>/", HabitUpdateApiView.as_view(), name="update_habit"),
    path("delete/<int:pk>/", HabitDestroyApiView.as_view(), name="delete_habit"),
]
