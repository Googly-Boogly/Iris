#****************************************************#
#  Status: Not bug tested
#****************************************************#

#++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Requirements:
#++++++++++++++++++++++++++++++++++++++++++++++++++++#

from app.global_code.helpful_functions import create_logger_error, CustomError, log_it, log_exceptions, \
    benchmark_and_log_exceptions
from app.commands.utilities.calendar_crud import create_google_calendar_event, edit_calendar_event,\
    delete_google_calendar_event, read_events_for_day, read_event_with_event_id, read_events_for_week
from app.commands.utilities.timer_module import create_timer
from app.commands.utilities.translator import translate_to, translate_from, detect_language
from app.commands.information.weather import get_current_weather_city, get_8day_forecast_city
from app.commands.entertainment.restaurants import get_restaurants_in_area
from app.commands.utilities.lights import switch_on_off, brightness_up, brightness_down, set_color,\
    wyze_turn_on, wyze_turn_off
from app.commands.utilities.tasks import create_task
from app.commands.utilities.habits import Habits_class
from app.commands.entertainment.music import select_and_play_album, select_and_play_artist, select_and_play_playlist,\
    select_and_play_song, skip_track, previous_track, shuffle_music, repeat_music
import os
from app.commands.entertainment.open_app import open_app
from app.commands.communication.texting import send_text_message_with_phone_num, send_text_message_with_name


def call_function(function_name: str, info: dict, global_variables: object) -> dict:
    """
    Switch statement
    will call the correct function based on the function name
    Is to be used with gpt3.5 return data
    :param function_name: the name of the function you want to call
    :param info: args and quarks of the function you need to call
    :param global_variables: global object of the project
    :return: dict with the anwser and the result of the function call
    """
    # CALENDAR
    if function_name == 'create_event':
        result = create_google_calendar_event(start_time=info['start_time'], start_date=info['start_date'],
                                              end_time=info['end_time'], end_date=info['end_date'],
                                              summary=info['summary'], description=info['description'],
                                              timezone_upload='America/Chicago', color_id=info['color_id'])
        data = {'anwser': True, 'result': result}
        return data
    elif function_name == 'edit_calendar_event':
        result = edit_calendar_event(event_id=info['event_id'], summary=info['summary'], description=info['description']
                                     , start_time=info['start_time'], end_time=info['end_time'])
        data = {'anwser': True, 'result': result}
        return data
    elif function_name == 'delete_event':
        result = delete_google_calendar_event(info['event_id'])
        data = {'anwser': True, 'result': result}
        return data
    elif function_name == 'read_events_for_day':
        result = read_events_for_day(info['event_id'])
        data = {'anwser': True, 'result': result}
        return data
    elif function_name == 'read_event_with_event_id':
        result = read_event_with_event_id(info['event_id'])
        data = {'anwser': True, 'result': result}
        return data
    elif function_name == 'read_events_for_week':
        result = read_events_for_week(info['date'])
        data = {'anwser': True, 'result': result}
        return data

    # TIMER
    elif function_name == 'create_timer':
        result = create_timer(global_variables=global_variables, name=info['name'], time=info['time'])
        data = {'anwser': True, 'result': result}
        return data

    # TRANSLATE
    elif function_name == 'translate_to':
        result = translate_to(target_language=info['target_language'], text=info['text'])
        data = {'anwser': True, 'result': result}
        return data
    elif function_name == 'translate_from':
        result = translate_from(source_language=info['source_language'], text=info['text'])
        data = {'anwser': True, 'result': result}
        return data
    elif function_name == 'detect_language':
        result = detect_language(text=info['text'])
        data = {'anwser': True, 'result': result}
        return data

    # WEATHER
    elif function_name == 'get_current_weather_city':
        result = get_current_weather_city(city=info['city'])
        data = {'anwser': True, 'result': result}
        return data
    elif function_name == 'get_8day_forecast_city':
        result = get_8day_forecast_city(city=info['city'])
        data = {'anwser': True, 'result': result}
        return data

    # RESTAURANTS
    elif function_name == 'get_restaurants_in_area':
        result = get_restaurants_in_area(latitude=info['latitude'], longitude=info['longitude'], radius=info['radius'])
        data = {'anwser': True, 'result': result}
        return data
    # LIGHTS
    elif function_name == 'switch_on_off':
        result = switch_on_off()
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'brightness_up':
        result = brightness_up()
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'brightness_down':
        result = brightness_down()
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'set_color':
        result = set_color(info['color'])
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'turn_lights_on':
        result = wyze_turn_on()
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'turn_lights_off':
        result = wyze_turn_off()
        data = {'anwser': False, 'result': result}
        return data
    # TASK
    elif function_name == 'create_task':
        result = create_task(task_name=info['task_name'], due_date=info['due_date'])
        data = {'anwser': False, 'result': result}
        return data
    # HABITS
    elif function_name == 'create_habit':
        result = Habits_class.create_habit(name=info['name'], due_time=info['due_time'], repeat_days=info['repeat_days']
                                           , priority=info['priority'],
                                           description=info['description'])
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'add_completed_habit':
        Habits_class.mark_done_for_day(info['habit_id'])
        result = Habits_class.add_completed_habit(info['habit_id'])
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'explain_all_habits':
        result = Habits_class.explain_all_habits()
        data = {'anwser': False, 'result': result, 'another_run?': True}
        return data
    # Music
    elif function_name == 'select_and_play_album':
        result = select_and_play_album(info['album_title'])
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'select_and_play_artist':
        result = select_and_play_artist(info['artist_name'])
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'select_and_play_playlist':
        result = select_and_play_playlist(info['playlist_title'])
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'select_and_play_song':
        result = select_and_play_song(info['song_title'])
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'skip_track':
        result = skip_track()
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'previous_track':
        result = previous_track()
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'shuffle_music':
        result = shuffle_music()
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'repeat_music':
        result = repeat_music()
        data = {'anwser': False, 'result': result}
        return data
    # phone open app
    elif function_name == 'open_app':
        result = open_app(info['app_name'])
        data = {'anwser': False, 'result': result}
        return data
    # Texting
    elif function_name == 'send_text_message_with_phone_num':
        result = send_text_message_with_phone_num(info['message'], info['phone_number'])
        data = {'anwser': False, 'result': result}
        return data
    elif function_name == 'send_text_message_with_name':
        result = send_text_message_with_name(info['message'], info['contact_name'])
        data = {'anwser': False, 'result': result}
        return data
    # elif function_name == 'edit_calendar_event':
    #     result = edit_calendar_event(message)
    #     return result
    # elif function_name == 'edit_calendar_event':
    #     result = edit_calendar_event(message)
    #     return result

    else:
        raise CustomError(f'Function name: {function_name} is not a valid function name')


if __name__ == '__main__':
    pass
