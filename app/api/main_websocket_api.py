import websockets
import asyncio
from app.key.keys import encrypt_message, decrypt_message
from app.websocket_server.testing_data import validate_data, validate_is_audio_data, test_data, test_data2, \
    validata_take_command_data
from app.utils.j_settings import Settings
from app.global_code.helpful_functions import create_logger_error, log_it
import os
from app.utils.chatgpt_api.chatgpt_api_calls import call_gpt


async def main_loop_api(settings: Settings):
    """
    The main loop of the server
    :return:
    """
    url = settings.websocket_url
    try:
        async with websockets.connect(url) as ws:
            authenticated = False
            while not authenticated:
                username = settings.username_api_decrypted
                await authenticate_api(ws, settings)
            await interact_with_main_server(ws, username)
    except websockets.exceptions.ConnectionClosed as e:
        logger = create_logger_error(os.path.abspath(__file__), 'main_loop', log_to_console=True)
        logger.info("Connection closed")


async def authenticate_api(websocket, settings: Settings) -> bool:
    """
    Authenticates the user
    :param settings: the settings object
    :param websocket: the websocket object
    :return: True if authenticated, False if not
    """
    username_decrypted = settings.username_api_decrypted
    username = encrypt_message(username_decrypted)

    response = await websocket.recv()

    await websocket.send(username)

    response = await websocket.recv()

    if response == "Please enter your password:":
        password_decrypted = settings.password_api_decrypted
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
    if message['data']['function_call'] == 'Iris':
        call_gpt(input_text=message['data']['speech_to_text'])


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main_loop_api())
