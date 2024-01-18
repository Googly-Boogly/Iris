from global_code.helpful_functions import connecttomysql, create_logger_error, log_it, log_exceptions
import os


class User:
    """
    This is a single user of the system. This class will hold all the information about the user.
    Will also interact with the database to save and load user information.
    """
    db = 'iris_v2_1'

    def __init__(self, data: dict):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.middle_name = data['middle_name']
        self.added = data['added']
        self.updated = data['updated']
        self.email = data['email']
        self.phone_number = data['phone_number']
        self.password = data['password']

    @staticmethod
    def save(data: dict):
        query = 'INSERT INTO users ' \
                '(first_name, last_name, middle_name, added, updated, email, phone_number, password)' \
                'VALUES (%(first_name)s, %(last_name)s, %(middle_name)s, %(added)s, %(updated)s, ' \
                '%(email)s, %(phone_number)s, %(password)s);'

        x = connecttomysql(User.db).query_db(query, data)
        return x

    @staticmethod
    @log_exceptions
    def select_all():
        raise 'e'
        query = 'SELECT * FROM users'

        x = connecttomysql(User.db).query_db(query)
        return x

    @staticmethod
    def select_one(specific_id: int):
        query = f'SELECT * FROM users WHERE id = {specific_id}'

        x = connecttomysql(User.db).query_db(query)
        return x


if __name__ == '__main__':
    data = {'user_id': '1', 'date': '2021-04-01', 'name': 'Main'}
    User.save(data)
    print(User.select_all())
