

from datetime import datetime, timedelta
import time
from database_scanner.alarm_checker import check_alarms
import os
from global_code.helpful_functions import create_logger_error, log_it, log_exceptions
from database_scanner.lights_checker import check_lights, do_lights
from database_scanner.reminders_checker import check_reminders
from utils.voice_output import speak
from commands.utilities.habits import Habits_class
import subprocess
import asyncio
# from commands.utilities.daily_todo import


def check_database() -> str or None:
    """
    loop for checking things in the database
    :return:
    """
    # new day check
    midnight_cycle()

    # rest of day checks
    alarm_check = check_alarms()
    if alarm_check[0]:
        # VERY VERY BUGGY CODE
        # Run the separate script as a separate process
        # powershell_script = r"F:\Coding\Iris_V2\database_scanner\create_alarm.ps1"
        # subprocess.Popen(["powershell", "-File", powershell_script], stdin=subprocess.PIPE,
        #                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 1TODO add alarm functionality
        pass

    check_light = check_lights()
    if check_light[0]:
        light_dict = check_light[1]
        do_lights(light_dict)
    check_reminder = check_reminders()
    if check_reminder[0]:
        speak(check_reminder[1]['to_say'])
        return check_reminder[1]['to_say']

    check_habits = Habits_class.check_habits()
    if check_habits[0]:
        speak(f"You have to do {check_habits[1]['name']}")
        return f"You have to do {check_habits[1]['name']}"
        # Send notification to phone


def run_database_loop_synchronous():
    """
    Loops through and checks the database for any of these "events" that will do something
    That could be turned on the lights or check alarms IE "events"
    Inside the if statements will be the code to actually do them
    :return: Runs forever
    """
    logger = create_logger_error(os.path.abspath(__file__), 'run_database_loop_synchronous')

    while True:
        try:

            alarm_check = check_alarms()

            if alarm_check[0]:
                # Run the separate script as a separate process
                powershell_script = r"F:\Coding\Iris_V2\database_scanner\create_alarm.ps1"
                process = subprocess.Popen(["powershell", "-File", powershell_script], stdin=subprocess.PIPE,
                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # stdout, stderr = process.communicate()
                # return_code = process.returncode
                # if return_code == 0:
                #     print("Separate script executed successfully")
                # else:
                #     print(f"Separate script returned an error (return code {return_code})")
                # script_file = 'create_alarm.ps1'
                # os.system(f'powershell -File "{script_file}"')
            check_light = check_lights()

            if check_light[0]:

                light_dict = check_light[1]
                do_lights(light_dict)
            check_reminder = check_reminders()
            if check_reminder[0]:
                speak(check_reminder[1]['to_say'])

        except Exception as e:
            log_it(logger, e)
        time.sleep(45)


def midnight_cycle():
    """
    called when it is a new day, will go over database and update anything that needs to be updated
    :return:
    """
    now = datetime.now()
    target_time = datetime(now.year, now.month, now.day, 0, 0)
    difference = now - target_time
    if timedelta(minutes=2) >= difference >= timedelta(minutes=-2):
        Habits_class.reset_for_day()


if __name__ == "__main__":
    pass
