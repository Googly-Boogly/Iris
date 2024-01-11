from app.commands.utilities.classes_utilities import alarms
from datetime import datetime, timedelta


def create_alarm_with_repeat(repeat_days: str, time: str, name: str = 'None', does_repeat: bool = True):
    """
    creates alarm in database
    :param repeat_days: (str) with the names of the days that it repeats EX: Monday Tuesday
    :param time: (str) EX 21:00 MAKE SURE IT HAS A 0 AT BEGGINING EX: 07:30 NOT 7:30
    :param name: name of the alarm
    :param does_repeat: (bool) true means does repeat false doesn't repeat
    :return: what sql gives back
    """
    data = {
        'name': name,
        'repeat_days': repeat_days,
        'end_time': time,
        'does_repeat': does_repeat,
        'added': datetime.now(),
        'updated': datetime.now(),
        'non_repeat_date': 'None'
    }
    return alarms.save(data)


def create_alarm_no_repeat(time: str, non_repeat_date: datetime, name: str = 'None', does_repeat: bool = False):
    """
    creates alarm in database
    :param time: (str) EX 21:00
    :param non_repeat_date: (datetime) the date of when alarm should go off in ISO 1801 format
    :param name: name of the alarm
    :param does_repeat: (bool) true means does repeat false doesnt repeat
    :return: what sql gives back
    """
    data = {
        'name': name,
        'repeat_days': '',
        'end_time': time,
        'does_repeat': does_repeat,
        'added': datetime.now(),
        'updated': datetime.now(),
        'non_repeat_date': non_repeat_date

    }
    alarms.save(data)


if __name__ == '__main__':
    # print(create_alarm_with_repeat(repeat_days='Monday Tuesday Wednesday Friday', time='07:30'))
    print(create_alarm_no_repeat(time='08:30', non_repeat_date=(datetime.now() + timedelta(days=1))))