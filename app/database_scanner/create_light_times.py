from app.commands.utilities.classes_utilities import lights
from datetime import datetime


# Database page
def create_light_alarm_with_repeat(on_off: bool, lights_color: str, lights_brightness: int, repeat_days: str,
                                   time: str, does_repeat: bool = True):
    """
    uploads to database with an alarm command with a repeat
    :param on_off: (bool) True = on False = off
    :param lights_color: (str) hexadecimal of the color
    :param lights_brightness: (int) 100 = max bright 0 = dimmest
    :param repeat_days: (str) string with the days it repeats ex: Monday Tuesday Thursday
    :param time: (str) of the time EX: 21:00
    :param does_repeat: (bool) True = does repeat False = doesn't
    :return: reply of the sql
    """
    data = {
        'on_off': on_off,  # True False (true=on)
        'lights_color': lights_color,
        'lights_brightness': lights_brightness,
        'repeat_days': repeat_days,
        'time': time,
        'does_repeat': does_repeat,
        'non_repeat_date': '',
        'added': datetime.now(),
        'updated': datetime.now(),
    }
    return lights.save(data)


def create_light_alarm(on_off: bool, lights_color: str, lights_brightness: int, time: str,
                       non_repeat_date: datetime,  does_repeat: bool = False):
    """
        uploads to database with a light command
        :param non_repeat_date: (datetime) when alarm should go off
        :param on_off: (bool) True = on False = off
        :param lights_color: (str) hexadecimal of the color
        :param lights_brightness: (int) 100 = max bright 0 = dimest
        :param time: (str) of the time EX: 21:00
        :param does_repeat: (bool) True = does repeat False = doesn't
        :return: reply of the sql
    """
    data = {
        'on_off': on_off, #True False (true=on)
        'lights_color': lights_color,
        'lights_brightness': lights_brightness,
        'time': time,
        'repeat_days': '',
        'does_repeat': does_repeat, # string with the days it repeats ex: Monday Tuesday Thursday
        'non_repeat_date': non_repeat_date,
        'added': datetime.now(),
        'updated': datetime.now(),
    }
    lights.save(data)


if __name__ == '__main__':
    #{'id': 7, 'name': 'None', 'end_time': '07:30', 'added': '2023-10-11 21:54:03.213338', 'updated': '2023-10-11 21:54:03.213338', 'does_repeat': 1, 'repeat_days': 'Monday Tuesday Wednesday Friday', 'non_repeat_date': 'None'}
    create_light_alarm_with_repeat(True, 'ffffff', 100, 'Monday Tuesday Wednesday Friday', '07:00', does_repeat=True)
    # create_light_alarm(True, 'ffffff', 100, '01:05', datetime.now())