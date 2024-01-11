from datetime import datetime, timedelta
from app.commands.utilities.classes_utilities import habit, completed_habit
from app.global_code.helpful_functions import create_logger_error, log_it, log_exceptions
import os


class Habits_class:
    def __init__(self):
        pass

    @staticmethod
    def mark_done_for_day(id: int) -> None:
        """
        marks a to do done in the database for the day
        :param id: (int) of the habit that is done
        :return:
        """
        total_habits = habit.select_all()
        for single_habit in total_habits:
            if id == single_habit['id']:
                data = {'id': single_habit['id'], 'done_for_day': True}
                habit.edit_done_for_day(data)

    @staticmethod
    def reset_for_day():
        total_habits = habit.select_all()
        for single_todo in total_habits:
            if single_todo['done_for_day']:
                data = {'id': single_todo['id'], 'done_for_day': False}
                habit.edit_done_for_day(data)

    @staticmethod
    @log_exceptions
    def explain_all_habits() -> list:
        """
        gets names of all todos if they are within 36000 seconds (10 hours)
        :return: (list) of all the (dict) names of the todos
        """
        curr_time = datetime.now()
        total_habits = habit.select_all()
        output = []
        for single_habit in total_habits:
            if not single_habit['done_for_day']:
                todo_time = datetime.strptime(single_habit['due_time'], "%H:%M")
                time_delta = curr_time - todo_time
                if time_delta.total_seconds() < 36000:
                    output.append({'name': single_habit['name'], 'id': single_habit['id']})
        return output

    @staticmethod
    @log_exceptions
    def ai_changes_to_todos(ais_guess_for_name_of_todo: str) -> bool:
        """
        check for guess of the name
        :param ais_guess_for_name_of_todo: (str) what the ai guesses the name of the habit
        :return: True if success else false
        """
        logger = create_logger_error(os.path.abspath(__file__), 'ai_changes_to_todos')
        try:
            check = False
            total_habits = habit.select_all()

            for single_habit in total_habits:
                if ais_guess_for_name_of_todo.lower() in single_habit['name']:
                    data = {'id': single_habit['id'], 'done_for_day': True}
                    habit.edit_done_for_day(data)
                    check = True
        except Exception as e:
            log_it(logger, e)
            return False
        return check

    @staticmethod
    @log_exceptions
    def create_habit(name: str, due_time: str, priority: str, repeat_days: str, description: str) -> str or bool:
        """

        :param description: (str) of the description of the habit
        :param name: (str) of name
        :param due_time: (str) of time INCLUDE 0 EX 08:30
        :param priority: (str) Low Medium High
        :param repeat_days: (str) include actual name of day EX Tuesday Thursday
        :return: (str) or (bool) based on the return of the sql
        """
        external = habit.save({'name': name,
                               'description': description,
                               'due_time': due_time,
                               'done_for_day': False,
                               'priority': priority,
                               'added': datetime.now(),
                               'updated': datetime.now(),
                               'repeat_days': repeat_days})
        return external

    @staticmethod
    @log_exceptions
    def add_completed_habit(habit_id: int) -> str or bool or None:
        """
        adds a completed habit to the database
        :param habit_id: (int)
        :return: NA
        """
        data = {
            'habit_id': habit_id,
            'added': datetime.now(),
            'updated': datetime.now()
        }
        return completed_habit.save(data)

    @staticmethod
    def check_habits() -> list:
        """
            returns False if no habit should go off
            :return: (list){bool, (dict)} if True habit reminder goes off
        """
        all_habits: list[dict] = habit.select_all()
        current_time = datetime.now()
        for single_habit in all_habits:
            time = single_habit['due_time']
            hours = int(time[:2])
            mins = int(time[3:])
            target_time = datetime(current_time.year, current_time.month, current_time.day, int(hours), int(mins))

            difference = current_time - target_time
            day_of_week = datetime.now().weekday()
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            current_day: str = days[day_of_week]
            # Finished preliminary variable creation

            # Checks if the habit is the same day, within 5 minutes of when the habit is, and if it has been reminded today

            if current_day.lower() in single_habit['repeat_days'].lower():
                if timedelta(minutes=5) >= difference >= timedelta(minutes=-5):
                    if single_habit['reminded'] == '0':
                        return [True, single_habit]
        return [False]


if __name__ == '__main__':
    # Habits_class.create_habit(name='Meditate', due_time='23:30', priority='High', repeat_days='Monday Tuesday Wednesday Thursday', description='meditate')
    Habits_class.add_completed_habit(20)
