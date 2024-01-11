from app.global_code.helpful_functions import connecttomysql, create_logger_error, log_it
import os


class timers:
    db = 'iris_v2_1'

    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.end_date = data['end_date']
        self.name = data['name']
        self.added = data['added']
        self.updated = data['updated']
        self.device_id = data['device_id']

    @staticmethod
    def save(data):
        logger = create_logger_error(os.path.abspath(__file__), 'timer.save')

        query = 'INSERT INTO timers ' \
                '(user_id, end_date, name, added, updated) ' \
                'VALUES (%(user_id)s, %(end_date)s, %(name)s, %(added)s, %(updated)s);'
        try:
            x = connecttomysql(timers.db).query_db(query, data)
            return x
        except Exception as e:
            log_it(logger, e)
            return None

    @staticmethod
    def select_all():
        logger = create_logger_error(os.path.abspath(__file__), 'timer.select_all')

        query = 'SELECT * FROM timers'
        try:
            x = connecttomysql(timers.db).query_db(query)
            return x
        except Exception as e:
            log_it(logger, e)
            return None


class alarms:
    db = 'iris_v2_1'

    def __init__(self, data):
        self.end_time = data['end_time']
        self.name = data['name']
        self.added = data['added']
        self.updated = data['updated']
        self.does_repeat = data['does_repeat']
        self.repeat_days = data['repeat_days']
        self.non_repeat_date = data['non_repeat_date']
        self.user_id = data['user_id']

    @staticmethod
    def save(data):
        query = 'INSERT INTO alarms ' \
                '(end_time, name, added, updated, does_repeat, repeat_days, non_repeat_date, user_id) ' \
                'VALUES (%(end_time)s, %(name)s, %(added)s, %(updated)s, %(does_repeat)s, ' \
                '%(repeat_days)s, %(non_repeat_date)s, %(user_id)s);'
        x = connecttomysql(alarms.db).query_db(query,data)
        return x

    @staticmethod
    def select_all():
        query = 'SELECT * FROM alarms'

        x = connecttomysql(timers.db).query_db(query)
        return x

    @staticmethod
    def delete(data):
        query = 'DELETE FROM alarms WHERE id = %(id)s'

        x = connecttomysql(alarms.db).query_db(query, data)
        return x


class lights:
    db = 'iris_v2_1'

    def __init__(self, data):
        self.on_off = data['on_off']
        self.lights_color = data['lights_color']
        self.lights_brightness = data['lights_brightness']
        self.does_repeat = data['does_repeat']
        self.time = data['time']
        self.repeat_days = data['repeat_days']
        self.non_repeat_date = data['non_repeat_date']
        self.added = data['added']
        self.updated = data['updated']

    @staticmethod
    def save(data):
        query = 'INSERT INTO lights ' \
                '(on_off, lights_color, lights_brightness, does_repeat, repeat_days, time, non_repeat_date,' \
                ' added, updated) ' \
                'VALUES (%(on_off)s, %(lights_color)s, %(lights_brightness)s, %(does_repeat)s, %(repeat_days)s, ' \
                '%(time)s, %(non_repeat_date)s, %(added)s, %(updated)s);'

        x = connecttomysql(lights.db).query_db(query,data)
        return x

    @staticmethod
    def select_all():
        query = 'SELECT * FROM lights'

        x = connecttomysql(lights.db).query_db(query)
        return x

    @staticmethod
    def delete(data):
        query = 'DELETE FROM lights WHERE id = %(id)s'

        x = connecttomysql(lights.db).query_db(query, data)
        return x


class reminders:
    db = 'iris_v2_1'

    def __init__(self, data):
        self.end_time = data['end_time']
        self.reminder = data['reminder']
        self.to_say = data['to_say']
        self.added = data['added']
        self.updated = data['updated']
        self.does_repeat = data['does_repeat']
        self.repeat_days = data['repeat_days']
        self.non_repeat_date = data['non_repeat_date']

    @staticmethod
    def save(data):
        query = 'INSERT INTO reminders ' \
                '(end_time, reminder, to_say, added, updated, does_repeat, repeat_days, non_repeat_date, user_id) ' \
                'VALUES (%(end_time)s, %(reminder)s, %(to_say)s, %(added)s, %(updated)s, %(does_repeat)s,' \
                ' %(repeat_days)s, %(non_repeat_date)s, %(user_id)s);'

        x = connecttomysql(reminders.db).query_db(query,data)
        return x

    @staticmethod
    def select_all():
        query = 'SELECT * FROM reminders'

        x = connecttomysql(reminders.db).query_db(query)
        return x

    @staticmethod
    def delete(data):
        query = 'DELETE FROM reminders WHERE id = %(id)s'

        x = connecttomysql(reminders.db).query_db(query, data)
        return x


class tasks:
    db = 'iris_v2_1'

    def __init__(self, data):
        self.due_date = data['due_date']
        self.task_name = data['task_name']
        self.description = data['description']
        self.priority = data['priority']
        self.status = data['status']
        self.added = data['added']
        self.updated = data['updated']
        self.user_id = data['user_id']

    @staticmethod
    def save(data):
        query = f'INSERT INTO tasks ' \
                f'(due_date, task_name, description, priority, status, added, updated, user_id)' \
                f' VALUES (%(due_date)s, %(task_name)s, %(description)s, %(priority)s, %(status)s, %(added)s,' \
                f' %(updated)s, %(user_id)s);'

        x = connecttomysql(tasks.db).query_db(query, data)
        return x

    @staticmethod
    def select_all():
        query = 'SELECT * FROM tasks'

        x = connecttomysql(tasks.db).query_db(query)
        return x

    @staticmethod
    def delete(data):
        query = f'DELETE FROM tasks WHERE id = %(id)s'

        x = connecttomysql(tasks.db).query_db(query, data)
        return x


class habit:
    db = 'iris_v2_1'

    def __init__(self, data):
        """
        uploads to database all data
        :param data:
        :param to_do: (str) of what needs to be done EX brush teeth
        :param due_time: (str) EX "08:30"; ALWAYS have a 0 at beggining if needed
        :param done_for_day: (bool) True = done
        :param priority: (str) low, medium, or high string
        """
        self.name = data['name']
        self.due_time = data['due_time']
        self.done_for_day = data['done_for_day']
        self.priority = data['priority']
        self.added = data['added']
        self.updated = data['updated']
        self.repeat_days = data['repeat_days']
        self.user_id = data['user_id']

    @staticmethod
    def save(data):
        query = f'INSERT INTO habit' \
                f' (name, due_time, done_for_day, priority, added, updated, repeat_days, user_id reminded)' \
                f' VALUES (%(name)s, %(due_time)s, %(done_for_day)s, %(priority)s, %(added)s, %(updated)s,' \
                f' %(repeat_days)s, %(user_id)s, False);'

        x = connecttomysql(tasks.db).query_db(query, data)
        return x

    @staticmethod
    def select_all():
        logger = create_logger_error(os.path.abspath(__file__), 'habit.select_all')

        query = 'SELECT * FROM habit'
        try:
            x = connecttomysql(tasks.db).query_db(query)
            return x
        except Exception as e:
            log_it(logger, e)
            return None

    @staticmethod
    def delete(data):
        logger = create_logger_error(os.path.abspath(__file__), 'habit.delete')

        query = f'DELETE FROM habit WHERE id = %(id)s'
        try:
            x = connecttomysql(tasks.db).query_db(query, data)
            return x
        except Exception as e:
            log_it(logger, e)
            return None

    @staticmethod
    def edit_done_for_day(data):
        logger = create_logger_error(os.path.abspath(__file__), 'habit.edit_done_for_day')

        query = """ UPDATE habit
                    SET done_for_day = %(done_for_day)s
                    WHERE id = %(id)s;
                """
        try:
            x = connecttomysql(tasks.db).query_db(query, data)
            return x
        except Exception as e:
            log_it(logger, e)
            return None

    @staticmethod
    def edit_reminded(data):
        logger = create_logger_error(os.path.abspath(__file__), 'habit.edit_done_for_day')

        query = """ UPDATE habit
                        SET reminded = %(reminded)s
                        WHERE id = %(id)s;
                    """
        try:
            x = connecttomysql(tasks.db).query_db(query, data)
            return x
        except Exception as e:
            log_it(logger, e)
            return None


class completed_habit:
    db = 'iris_v2_1'

    def __init__(self, data):
        """
        uploads to database all data
        :param data:
        :param habit_id: (int)
        """
        self.habit_id = data['habit_id']
        self.added = data['added']
        self.updated = data['updated']

    @staticmethod
    def save(data):
        logger = create_logger_error(os.path.abspath(__file__), 'completed_habit.save')

        query = f'INSERT INTO completed_habit (habit_id, added, updated) VALUES (%(habit_id)s, %(added)s, %(updated)s);'

        try:
            x = connecttomysql(tasks.db).query_db(query, data)
            return x
        except Exception as e:
            log_it(logger, e)
            return None

    @staticmethod
    def select_all():
        logger = create_logger_error(os.path.abspath(__file__), 'completed_habit.select_all')

        query = 'SELECT * FROM completed_habit'
        try:
            x = connecttomysql(tasks.db).query_db(query)
            return x
        except Exception as e:
            log_it(logger, e)
            return None
