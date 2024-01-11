# ****************************************************#
#  Status: currently bug testing
# ****************************************************#


# ++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Requirements:
# ++++++++++++++++++++++++++++++++++++++++++++++++++++#
import openai
from app.global_code.helpful_functions import create_logger_error, log_it, log_exceptions,\
    benchmark_and_log_exceptions, benchmark_function
import json
from app.utils.function_caller import call_function
from app.utils.voice_output import speak
from app.utils.chatgpt_api.functions import get_list_of_functions
from app.global_code.secrets import openai_api_key
from app.global_code.global_vars import get_current_details
import os


def create_api_key():
    api_key = openai_api_key()
    openai.api_key = api_key
    return api_key


@log_exceptions
def generate_response(prompt: str, input_text: str) -> str:
    """
    This function will generate a response from the prompt and the input_text
    This is used to continue the conversation
    :param prompt:
    :param input_text:
    :return:
    """
    create_api_key()
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Current details of the user {get_current_details()}. The user said this {input_text}: than we got this information {prompt}. Summarize the information",
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()


@log_exceptions
def call_api_function_call(message: str) -> openai:
    """
    This function will call the GPT-3 API and return the response
    Using any functions you provide and decide to call a function or return a normal gpt response
    :param message: The thing that was said
    :return: What the API returned
    """
    api_key = create_api_key()
    responses = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-0613',
        messages=[{'role': 'user', 'content': message}, {"role": 'system',
                                                         'content': f"Current details of the "
                                                         f"user {get_current_details()}. "
                                                         f"Dont make up any functions, make the response "
                                                         f"brief, ask for values if anything is ambiguous."}],

        functions=get_list_of_functions(),
        function_call='auto'
    )
    print(type(responses))
    print(responses)
    return dict(str(responses))


# @log_exceptions
def call_gpt(input_text: str, global_variables: list or None = None) -> None:
    """
    This function will call the GPT-3 API and return the response
    Using any functions you provide and decide to call a function or return a nromal gpt response
    :param input_text: The thing that was said
    :return: NA
    """
    responses: openai = call_api_function_call(input_text)
    message3 = responses['choices']
    message = message3[0]['message']
    print(f"Message: {message}")

    tokens_used: int = responses['usage']['total_tokens']

    finish_reason: str = responses['choices'][0]['finish_reason']
    ai_reply: str = responses['choices'][0]['message']['content']

    if finish_reason == 'function_call':
        name_of_function: str = responses['choices'][0]['message']['function_call']['name']
        print(f"name of function: {name_of_function}")
        arguments = json.loads(responses['choices'][0]['message']['function_call']['arguments'])
        temp = call_function(function_name=name_of_function, info=arguments, global_variables=global_variables)
        print(f"call_function return: {temp['result']}")
        print(f"tokens_used: {tokens_used}")
        print(f"AI Response: {ai_reply}")
        if temp['anwser']:
            ai_return = generate_response(temp['result'], input_text)
            print(f"AI Return: {ai_return}")
            speak(ai_return)

    else:
        print(f"tokens_used: {tokens_used}")
        print(f"AI Response: {ai_reply}")
        speak(ai_reply)


if __name__ == '__main__':
    pass
