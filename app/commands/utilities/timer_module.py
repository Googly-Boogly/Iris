from commands.utilities.classes_utilities import timers
from datetime import datetime, timedelta
from global_code.helpful_functions import create_logger_error, log_it, log_exceptions

#****************************************************#
#  Status: Discontinued
#****************************************************#


@log_exceptions
def create_timer(global_variables: dict, name: str, time: dict) -> bool:
    """ time is a dictonary of either end_of_timer key, which is a datetime of when the timer goes off
    the dict could also have finished_in key, which is dictonary which has these key; hours, minutes, seconds, days
    the finished_in could be in 5 minutes which this function creates a datetime value of the end of the timer
    """

    if time["type"] == 'end_of_timer':
        # upload into database
        data = {
            'user_id': global_variables['user_id'],
            'name': name,
            'end_date': time
        }
        timers.save(data)
    elif time["type"] == 'finished_in':
        # add up all the time delta and create a final time
        now = datetime.now()

        final_time = now + timedelta(days=time['days'])
        final_time = final_time + timedelta(hours=time['hours'])
        final_time = final_time + timedelta(minutes=time['minutes'])
        final_time = final_time + timedelta(seconds=time['seconds'])
        data = {
            'user_id': global_variables['user_id'],
            'name': name,
            'end_date': final_time
        }
        timers.save(data)

    return True


# x = create_timer({'user_id': 1}, "timer1", {'type': 'finished_in', 'days': 0, 'hours': 0, 'minutes': 1, 'seconds': 1})
# print(x)