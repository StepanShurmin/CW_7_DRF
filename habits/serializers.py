from rest_framework import serializers
from habits.models import Habit
from habits.validators import (
    AssociatedHabitAndRewardValidator,
    ExecutionTimeValidator,
    AssociatedHabitValidator,
    IsNiceValidator,
    ExecutionPeriodicityValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        extra_kwargs = {"user": {"required": False}}
        validators = [
            AssociatedHabitAndRewardValidator(field_1="associated_habit", field_2="reward"),
            ExecutionTimeValidator(field="execution_time"),
            AssociatedHabitValidator(field="associated_habit"),
            IsNiceValidator(field_1="associated_habit", field_2="is_nice", field_3="reward"),
            ExecutionPeriodicityValidator(field="periodicity"),
        ]
