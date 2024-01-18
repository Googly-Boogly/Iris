from datetime import datetime, timedelta
from commands.utilities.classes_utilities import reminders
from global_code.helpful_functions import create_logger_error, log_it, log_exceptions
import os


def retrieve_reminders():
    all_rem = reminders.select_all()
    return all_rem


def check_reminders() -> list:
    """
    returns False if no light should go on/off,
    :return: (list) if light should go off (bool), light data from database (dict)
    """
    now = datetime.now().isoformat()
    all_reminds = retrieve_reminders()
    current_time = datetime.now()
    # Specify the target time

    for reminder in all_reminds:
        time = reminder['end_time']
        # datetime objects
        hours = int(time[:2])
        mins = int(time[3:])
        target_time = datetime(current_time.year, current_time.month, current_time.day, int(hours), int(mins))

        difference = current_time - target_time
        day_of_week = datetime.now().weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        current_day = days[day_of_week]
        # Finished preliminary variable creation

        if reminder['does_repeat']:
            if current_day.lower() in reminder['repeat_days'].lower():
                if timedelta(minutes=5) >= difference >= timedelta(minutes=-5):
                    return [True, reminder]
        else:
            # checks if current time is past the end time of the alarm
            data = {
                'id': reminder['id']
            }
            reminders.delete(data)
            return [True, reminder]
    return [False]


if __name__ == "__main__":
    pass
