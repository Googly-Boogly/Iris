#****************************************************#
#  Status: translate to and from work
#****************************************************#

#++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Known Bugs: Detect_language doesn't work
#++++++++++++++++++++++++++++++++++++++++++++++++++++#

#++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Requirements:
#++++++++++++++++++++++++++++++++++++++++++++++++++++#

from global_code.helpful_functions import create_logger_error, log_it, log_exceptions
import os


@log_exceptions
def detect_language(text: str) -> str:
    """
    detects the language of the text
    :type text: text to detect the language of
    :return: the language of the text
    """
    pass


@log_exceptions
def translate_to(target_language: str, text: str) -> str:
    """
    translates the text to the target language
    :param target_language: target language EXAMPLE: en, es, fr
    :param text: text to translate
    :return: translated text
    """


@log_exceptions
def translate_from(source_language: str, text: str) -> str:
    """
    translates the text from the source language to english
    :param source_language: source language EXAMPLE: en, es, fr
    :param text: text to translate
    :return: translated text
    """


if __name__ == '__main__':
    text = "Hola, cómo estás?"
    detected_lang = detect_language(text)
    print(detected_lang)  # Output: 'es' (which represents Spanish)
