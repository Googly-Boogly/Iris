from datetime import datetime, timedelta
from app.commands.utilities.classes_utilities import lights
from app.commands.utilities.lights import brightness_down, brightness_up, set_color, wyze_turn_on, wyze_turn_off
from app.global_code.helpful_functions import log_exceptions, benchmark_function, benchmark_and_log_exceptions
import os


def retrieve_lights():
    all_lights = lights.select_all()
    return all_lights


def check_lights() -> list:
    """
    returns False if no light should go on/off,
    :return: (list) if light should go off (bool), light data from database (dict)
    """

    now = datetime.now().isoformat()
    all_lights = retrieve_lights()
    current_time = datetime.now()
    # Specify the target time

    for light in all_lights:
        time = light['time']
        # datetime objects
        hours = int(time[:2])
        mins = int(time[3:])
        target_time = datetime(current_time.year, current_time.month, current_time.day, int(hours), int(mins))

        difference = current_time - target_time
        day_of_week = datetime.now().weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        current_day = days[day_of_week]
        # Finished preliminary variable creation

        if light['does_repeat'] == '1':

            if current_day.lower() in light['repeat_days'].lower():
                if timedelta(minutes=5) >= difference >= timedelta(minutes=-5):
                    return [True, light]
        else:
            if timedelta(minutes=15) >= difference >= timedelta(minutes=-5):
        # checks if current time is past the end time of the alarm
                data = {
                    'id': light['id']
                }
                lights.delete(data)
                return [True, light]
    return [False]


def do_lights(dict_list: dict):
    if not dict_list['on_off']:
        wyze_turn_off()
    else:
        wyze_turn_on()
        set_color(dict_list['lights_color'])
        if dict_list['lights_brightness'] > 50:
            brightness_up()
        else:
            brightness_down()


if __name__ == "__main__":
    pass
