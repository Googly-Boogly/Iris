from app.utils.speech_input_loop import main
from app.utils.chatgpt_api.chatgpt_api_calls import call_gpt
import asyncio
from app.database_scanner.loop import run_database_loop_asynchronous
from app.websocket_server.main_websocket import main_loop
from app.global_code.helpful_functions import log_exceptions, benchmark_function,\
    benchmark_and_log_exceptions, count_lines_of_code
from app.utils.j_settings import Settings
from app.utils.user_classes import User
from app.api.main_websocket_api import main_loop_api
from datetime import datetime


if __name__ == "__main__":
    """
    This will create 2 async threads that will run the main loop of the server, one will scan the database and the other
    will server as an api for the chatbot
    """
    # print(count_lines_of_code(r'F:\Coding\Iris_V2\app'))
    user_data = User.select_one(1)
    user_data = user_data[0]

    user = User(
        {'id': 1, 'first_name': user_data['first_name'], 'last_name': user_data['last_name'],
         'middle_name': user_data['middle_name'], 'added': user_data['added'], 'updated': user_data['updated'],
         'email': user_data['email'], 'phone_number': user_data['phone_number'], 'password': user_data['password']}
    )
    setting = Settings(current_latitude=0, current_longitude=0,
                       current_city='test', current_state='test', current_country='test',
                       current_zipcode=55446, current_timezone='test',
                       user=user)
    loop = asyncio.get_event_loop()
    tasks = [main_loop(setting), main_loop_api(setting)]
    loop.run_until_complete(asyncio.gather(*tasks))
    # print(count_lines_of_code(r'F:\Coding\Iris_V2\app'))
    # they_loop()
    # single_test()

    # print(datetime.now())