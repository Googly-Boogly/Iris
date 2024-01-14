import websockets
import asyncio
from app.key.keys import encrypt_message, decrypt_message
from app.websocket_server.testing_data import validate_data, validate_is_audio_data, test_data, test_data2, \
    validata_take_command_data
from app.utils.j_settings import Settings
from app.global_code.helpful_functions import create_logger_error, log_it, CustomError
from app.websocket_server.database_scanner_websocket import check_database
import os
from app.global_code.global_vars import get_current_details


async def main_loop(settings: Settings):
    """
    The main loop of the server
    :return:
    """
    url = settings.websocket_url
    try:
        async with websockets.connect(url) as ws:
            authenticated = False
            while not authenticated:
                username = settings.username_async_thread_decrypted
                authenticated = await authenticate(ws, settings)
            await interact_with_main_server(ws, username)
    except websockets.exceptions.ConnectionClosed as e:
        logger = create_logger_error(os.path.abspath(__file__), 'main_loop', log_to_console=True)
        print(e)
        logger.info("Connection closed")


async def authenticate(websocket, settings: Settings) -> bool:
    """
    Authenticates the user
    :param settings: the settings object
    :param websocket: the websocket object
    :return: True if authenticated, False if not
    """
    username_decrypted = settings.username_async_thread_decrypted
    username = encrypt_message(username_decrypted)

    response = await websocket.recv()
    await websocket.send(username)

    response = await websocket.recv()
    if response == "Please enter your password:":
        password_decrypted = settings.password_async_thread_decrypted
        password = encrypt_message(password_decrypted)

        await websocket.send(password)

        response = await websocket.recv()

        if response == "Authentication successful. You are now connected.":
            return True
    return False


async def interact_with_main_server(ws, username):
    """
    Once connected to the main server will send data and receive data
    :param ws:
    :param username:
    :return:
    """
    logger = create_logger_error(os.path.abspath(__file__), 'interact_with_main_server', log_to_console=True)
    while True:
        what_to_say = check_database()
        if what_to_say is None:
            await ws.send('ping')
            check = await ws.recv()
            if check != 'pong':
                raise CustomError('Unexpected Websocket message')
            continue
        await ws.send(str(test_data2()))
        msg = await ws.recv()
        try:
            do_message(msg)
        except AssertionError as e:
            logger.info("Invalid message type")
            log_it(logger, e)
        #


def do_message(message: dict) -> bool:
    """
    Will direct the incoming data to the correct function
    IF ping will return True
    :param message: the incoming data (probably json)
    :return: true if its a ping
    """

    if message['ping'] == 'ping':
        print('ping')
        return True
    validata_take_command_data(message)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main_loop(get_current_details()))
