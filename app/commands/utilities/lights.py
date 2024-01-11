from wyze_sdk import Client
from app.global_code import secrets
from app.global_code.helpful_functions import create_logger_error, log_it, log_exceptions
import os


def create_client():
    client = Client(email=secrets.wyze_email(), password=secrets.wyze_password(), api_key=secrets.wyze_api_key(),
                    key_id=secrets.wyze_key_id())
    return client


def get_info() -> object:
    client = create_client()
    x: object = client.bulbs.info(device_mac='D03F2799B407', device_model='HL_LSLP')
    return x


@log_exceptions
def wyze_turn_on():
    client = create_client()
    y = client.bulbs.turn_on(device_mac='D03F2799B407', device_model='HL_LSLP')


@log_exceptions
def wyze_turn_off():
    client = create_client()
    y = client.bulbs.turn_off(device_mac='D03F2799B407', device_model='HL_LSLP')


def color_white():
    client = create_client()
    y = client.bulbs.set_color(device_mac='D03F2799B407', device_model='HL_LSLP', color='ffffff')


def set_brightness(brightness: int):
    """

    :param brightness: int of the brightness
    :return:
    """
    client = create_client()
    y = client.bulbs.set_brightness(device_mac='D03F2799B407', device_model='HL_LSLP', brightness=brightness)


@log_exceptions
def switch_on_off() -> bool:
    info = get_info()

    if info.is_on:
        wyze_turn_on()
    else:
        wyze_turn_off()
        # wyze_turn_on()
    return True


@log_exceptions
def set_color(color):
    """

    :param color: (str) of the hexadeimal of the color
    :return:
    """
    client = create_client()
    y = client.bulbs.set_color(device_mac='D03F2799B407', device_model='HL_LSLP', color=color)
    return True


@log_exceptions
def brightness_down():
    client = create_client()
    y = client.bulbs.set_brightness(device_mac='D03F2799B407', device_model='HL_LSLP', brightness=10)
    return True


@log_exceptions
def brightness_up() -> bool:
    client = create_client()
    y = client.bulbs.set_brightness(device_mac='D03F2799B407', device_model='HL_LSLP', brightness=100)
    return True



def create_lights_with_repeat():
    pass


def create_lights_no_repeat():
    pass


if __name__ == '__main__':
    # switch_on_off()
    # wyze_turn_on()
    # brightness_up()
    # brightness_down()
    # set_color('ffffff') #hexadecimal
    pass