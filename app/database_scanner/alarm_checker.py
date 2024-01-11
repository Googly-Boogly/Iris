from datetime import datetime, timedelta
from app.commands.utilities.classes_utilities import alarms
from app.global_code.helpful_functions import log_exceptions, benchmark_function, benchmark_and_log_exceptions
import os


def retrieve_alarms():
    all_alarms = alarms.select_all()
    return all_alarms


def check_alarms() -> list:
    """
    scans database to see if any alarms should go off
    returns False if no alarm should go off, True if one should
    :return: if alarm should go off (bool)
    """

    now = datetime.now().isoformat()
    all_alarms = retrieve_alarms()
    current_time = datetime.now()
    # Specify the target time

    for alarm in all_alarms:
        time = alarm['end_time']
        # datetime objects
        hours = int(time[:2])
        mins = int(time[3:])

        target_time = datetime(current_time.year, current_time.month, current_time.day, int(hours), int(mins))

        difference = current_time - target_time

        day_of_week = datetime.now().weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Get the string representation of the current day
        current_day = days[day_of_week]

        if alarm['does_repeat']:

            if current_day.lower() in alarm['repeat_days'].lower():
                if timedelta(minutes=5) >= difference >= timedelta(minutes=-5):
                    # if current_day.lower() in alarm['repeat_days'].lower():
                    return [True, alarm]
        else:
            if timedelta(minutes=5) >= difference >= timedelta(minutes=-5):
                data = {'id': alarm['id']}
                alarms.delete(data)
                return [True, alarm]
    return [False]


if __name__ == "__main__":
    print(check_alarms())
    # now = datetime.now()
    # time.sleep(1)
    # now2 = datetime.now()
    # if now > now2:
    #     print('false')