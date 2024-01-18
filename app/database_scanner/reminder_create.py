from commands.utilities.classes_utilities import reminders
from datetime import datetime


def create_reminder_with_repeat(time: str, repeat_days: str, reminder: str, to_say: str, does_repeat: bool = True):
    """
    creates reminder in database
    :param reminder: (str) name of the reminder
    :param to_say: (str) what virtual assisstant should say
    :param repeat_days: (str) string with the days that repeat EX: Monday Tuesday
    :param time: (str) time when it should go off; EX: 21:00 DO NOT do 7:30 DO 07:30
    :param does_repeat: (bool) if it repeats
    :return: sql gives back
    """
    data = {
        'reminder': reminder,
        'to_say': to_say,
        'repeat_days': repeat_days,
        'end_time': time,
        'does_repeat': does_repeat,
        'added': datetime.now(),
        'updated': datetime.now(),
        'non_repeat_date': ''

    }
    return reminders.save(data)


def create_reminder_no_repeat(reminder: str, to_say: str, non_repeat_date: datetime,
                              time: str, does_repeat: bool = False):
    """
    creates reminder in database
    :param reminder: (str) name of the reminder
    :param to_say: (str) what virtual assisstant should say
    :param non_repeat_date: (datetime) of just the date not the time when it should go off
    :param time: (str) time when it should go off; EX: 21:00 DO NOT do 7:30 DO 07:30
    :param does_repeat: (bool) if it repeats
    :return: sql gives back
    """

    data = {
        'reminder': reminder,
        'to_say': to_say,
        'repeat_days': '',
        'end_time': time,
        'does_repeat': does_repeat,
        'added': datetime.now(),
        'updated': datetime.now(),
        'non_repeat_date': non_repeat_date

    }
    x = reminders.save(data)
    return x


if __name__ == '__main__':
    print(create_reminder_no_repeat(reminder='Do the dishes', to_say='DO THE DISHES BITCH', time='21:40', non_repeat_date=(datetime.now())))
    # print(create_reminder_with_repeat(reminder='Do the Dishes', to_say='Its that time again DO THE DISHES', time='14:00', repeat_days='Sunday'))
    pass