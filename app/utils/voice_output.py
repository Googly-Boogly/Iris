import pyttsx3
import sounddevice as sd
from app.global_code.helpful_functions import create_logger_error, log_it, benchmark_and_log_exceptions
from app.utils.j_settings import Settings

def get_output_device_index(device_name: str or None) -> int or None:
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if device['name'] == device_name:
            return i
    return None


@benchmark_and_log_exceptions
def speak(text: str, device_name: str or None = None, settings: Settings or None = None) -> str:
    """
    This will be redesigned to create mp3 files, playing them will be up to the device
    Speaks the text
    :param text: the text to speak
    :return: mp3 file directory
    """
    engine = pyttsx3.init()
    output_device_index: int | None = get_output_device_index(device_name)
    print(output_device_index)
    if output_device_index is not None:
        engine.setProperty('driverName', 'sounddevice')
        engine.setProperty('audioOutput', output_device_index)

    engine.say(text)
    engine.runAndWait()
    return ''


def create_mp3_file_with_speech(text: str, settings: Settings) -> str:
    """
    creates a mp3 file with the text default directory is path_to_file_directory/mp3_file_download/
    :param settings: the Settings object for the user
    :param text: the text to speak
    :return: mp3 file directory
    """
    directory_for_mp3 = settings.directory_for_mp3

if __name__ == '__main__':
    speak("Hello, my name is Alex", "Pebble Speakers (High Definitio")
# Specify the desired device name
# device_name = "Pebble Speakers (High Definitio"
#
# # List available sound devices
# print(sd.query_devices())
#
# speak("Hello, my name is Alex", device_name)
