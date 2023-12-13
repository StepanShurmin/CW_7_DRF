from rest_framework.serializers import ValidationError


class AssociatedHabitAndRewardValidator:
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        associated_habit = dict(value).get(self.field_1)
        reward = dict(value).get(self.field_2)

        if associated_habit and reward:
            raise ValidationError(f"Нельзя одновременно выбирать {self.field_1} и {self.field_2}.")


class ExecutionTimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        execution_time = dict(value).get(self.field)
        if isinstance(execution_time, int) and execution_time > 120:
            raise ValidationError(f"Время выполнения должно быть не больше 120 секунд.")


class AssociatedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        associated_habit = dict(value).get(self.field)

        if associated_habit and not associated_habit.is_nice:
            raise ValidationError(f"В связанные привычки могут попадать только привычки с признаком приятной привычки.")


class IsNiceValidator:
    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        associated_habit = dict(value).get(self.field_1)
        is_nice = dict(value).get(self.field_2)
        reward = dict(value).get(self.field_3)

        if is_nice and (reward or associated_habit):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


class ExecutionPeriodicityValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = dict(value).get(self.field)
        if isinstance(periodicity, int) and periodicity > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
