from app.utils.user_classes import User
import os
from typing import Optional


class Settings:
    """
    Singleton Class:
    This class will hold the settings for the user
    Will act as the apps state
    """
    def __init__(self, current_latitude: float, current_longitude: float, current_city: str,
                 current_state: str, current_country: str, current_zipcode: int,
                 current_timezone: str, user: User, directory_for_mp3: Optional[str] = None,
                 username_async_thread_decrypted: Optional[str] = None,
                 password_async_thread_decrypted: Optional[str] = None, username_api_decrypted: Optional[str] = None,
                 password_api_decrypted: Optional[str] = None, websocket_url: Optional[str] = None,
                 ip: Optional[str] = None, port: Optional[str] = None):
        """
        All settings for the user
        :param current_latitude: current latitude of the user
        :param current_longitude: current longitude of the user
        :param current_city: current city of the user
        :param current_state: current state of the user
        :param current_country: current country of the user
        :param current_zipcode: current zipcode of the user
        :param current_timezone: current timezone of the user
        :param user: the User object
        :param directory_for_mp3: change directory where mp3 files are downloaded
        :param username_async_thread_decrypted: websocket username for the async thread connection
        :param password_async_thread_decrypted: websocket password for the async thread connection
        :param username_api_decrypted: websocket username for the api connection
        :param password_api_decrypted: websocket password for the api connection
        :param websocket_url: websocket url
        """
        self.current_latitude = current_latitude
        self.current_longitude = current_longitude
        self.current_city = current_city
        self.current_state = current_state
        self.current_country = current_country
        self.current_zipcode = current_zipcode
        self.current_timezone = current_timezone
        self.user = user
        self.ip = ip if ip else os.getenv('IP')
        self.port = port if port else os.getenv('PORT')
        self.directory_for_mp3 = directory_for_mp3 if directory_for_mp3 \
            else os.path.dirname(__file__) + '/mp3_file_download/'

        # 1TODO Change username and password here in production
        # main_websockets.py
        self.username_async_thread_decrypted = username_async_thread_decrypted if username_async_thread_decrypted\
            else 'async_thread'
        self.password_async_thread_decrypted = password_async_thread_decrypted if password_async_thread_decrypted\
            else 'ASYNC_IS_GR8_567%'
        self.username_api_decrypted = username_api_decrypted if username_api_decrypted else 'api_server'
        self.password_api_decrypted = password_api_decrypted if password_api_decrypted else 'API_SERVER_PASSWORD123#'
        self.websocket_url = websocket_url if websocket_url else f'ws://{self.ip}:{self.port}'

    def update_details(self):
        """
        This will update the current details of the user with the database)
        :return: None
        """


def get_current_details_test():
    user = User(
        {'id': 1, 'first_name': 'test', 'last_name': 'test',
         'middle_name': 'test', 'added': 'test', 'updated': 'test',
         'email': 'test', 'phone_number': 'test', 'password': 'test'}
    )
    setting = Settings(current_latitude=0, current_longitude=0,
                       current_city='test', current_state='test', current_country='test',
                       current_zipcode=55446, current_timezone='test',
                       user=user)
    return setting


if __name__ == '__main__':
    pass
