#****************************************************#
#  Status: translate to and from work
#****************************************************#

#++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Known Bugs: Detect_language doesn't work
#++++++++++++++++++++++++++++++++++++++++++++++++++++#

#++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Requirements:
#++++++++++++++++++++++++++++++++++++++++++++++++++++#

from google.cloud import translate_v2 as translate
from googletrans import Translator
from app.global_code.helpful_functions import create_logger_error, log_it, log_exceptions
from app.global_code.secrets import detect_language_google_api_key
import os


@log_exceptions
def detect_language(text: str) -> str:
    """
    detects the language of the text
    :type text: text to detect the language of
    :return: the language of the text
    """
    api_key2 = detect_language_google_api_key()
    client = translate.Client(api_key=api_key2)
    result = client.detect_language(text)
    detected_lang = result['language']
    return detected_lang


@log_exceptions
def translate_to(target_language: str, text: str) -> str:
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    translated_text = translation.text
    return translated_text


@log_exceptions
def translate_from(source_language: str, text: str) -> str:
    translator = Translator()
    translation = translator.translate(text, src=source_language, dest='en')
    translated_text = translation.text
    return translated_text


if __name__ == '__main__':
    text = "Hola, cómo estás?"
    detected_lang = detect_language(text)
    print(detected_lang)  # Output: 'es' (which represents Spanish)
