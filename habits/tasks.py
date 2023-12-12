from datetime import datetime, timedelta

from celery import shared_task


from habits.models import Habit
from habits.services import send_message, get_updates, parse_updates
from users.models import User


@shared_task
def get_message_data():
    time_now = datetime.now()
    start_time = time_now - timedelta(minutes=10)
    finish_time = time_now + timedelta(minutes=10)
    habits = Habit.objects.filter(time__gte=start_time).filter(time__lte=finish_time)

    for h in habits:
        action = h.action
        place = h.place
        time = h.time
        periodicity = h.periodicity
        execution_time = h.execution_time
        username = h.user.name
        user_tg = h.user.tlg_info

        updates = get_updates()
        if updates["ok"]:
            parse_updates(updates["result"])

        chat_id = User.objects.get(tlg_info=user_tg).chat_id

        text = f'Необходимо выполнить {action} в {time.strftime("%H:%M")} в {place}'
        send_message(text, chat_id)

        time += timedelta(days=periodicity)
        h.save()
