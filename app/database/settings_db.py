from app.global_code.helpful_functions import connecttomysql, create_logger_error, log_it
import os


class db_settings:
    """
    db class for settings
    """
    db = 'iris_v2_1'

    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.end_date = data['end_date']
        self.added = data['added']
        self.updated = data['updated']

    @staticmethod
    def save(data):
        query = 'INSERT INTO settings ' \
                '(user_id, added, updated) ' \
                'VALUES (%(user_id)s, %(added)s, %(updated)s);'
        x = connecttomysql(timers.db).query_db(query, data)
        return x

    @staticmethod
    def select_all_where(user_id: int):
        query = f'SELECT * FROM settings WHERE user_id = {user_id}'

        x = connecttomysql(timers.db).query_db(query)
        return x

