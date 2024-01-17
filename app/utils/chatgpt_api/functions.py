import unittest


def get_list_of_functions() -> list[dict]:
    """
    Unit test to make sure all the functions are valid
    :return: a list of all the functions available to the user
    """
    total_functions = list_of_functions()
    validate_total_functions(total_functions)
    return total_functions


def validate_total_functions(total_functions):
    for function in total_functions:
        unit_test_validate_function(function)


@unittest.expectedFailure
def unit_test_validate_function(function: dict):
    # UNIT TEST FUNCTION
    # example func
    """
    function = {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    }
    """

    # Check the presence of required key and their types
    assert "name" in function and isinstance(
        function["name"], str
    ), "'name' must be a string."
    assert "description" in function and isinstance(
        function["description"], str
    ), "'description' must be a string."
    assert "parameters" in function and isinstance(
        function["parameters"], dict
    ), "'parameters' must be a dictionary."

    # Check the structure of 'parameters' key
    params = function["parameters"]

    assert (
            "type" in params and params["type"] == "object"
    ), "'type' must be 'object' in parameters."
    assert "properties" in params and isinstance(
        params["properties"], dict
    ), "'properties' must be a dictionary."
    assert "required" in params and isinstance(
        params["required"], list
    ), "'required' must be a list."

    # Check the structure of 'properties' in 'parameters'
    for key, prop in params["properties"].items():
        assert "type" in prop and isinstance(
            prop["type"], str
        ), f"'type' must be a string in properties of {key}."

        if prop["type"] == "array":
            assert (
                    "items" in prop
            ), f"'items' must be present in properties of {key} when type is 'array'."

        # Enum check only if it exists
        if "enum" in prop:
            assert isinstance(
                prop["enum"], list
            ), f"'enum' must be a list in properties of {key}."

    # Check 'required' properties are in 'properties'
    for key in params["required"]:
        assert (
            key in params["properties"]
        ), f"'{key}' mentioned in 'required' must exist in 'properties'."


def list_of_functions() -> list[dict]:
    """
    This function will return a list of all the functions that are available to the user
    These functions will be given to the gpt to decide if it needs to be called or not
    :return: a list of dicts of all the functions
    """
    function_create_event = {
            "name": 'create_event',
            "description": 'create a calendar event',
            "parameters": {
                "type": 'object',
                'properties': {
                    "start_time": {
                        'type': 'string',
                        'description': 'datetime of the start of the event',
                    },
                    'end_time': {
                        'type': 'string',
                        'description': 'datetime of the end of the event',
                    },
                    'summary': {
                        'type': 'string',
                        'description': 'title of the event',
                    },
                    'description': {
                        'type': 'string',
                        'description': 'description of the event including any details that are known',
                    }
                },
                'required': ['start_time', 'end_time', 'summary']
            },

        }
    function_edit_calendar_event = {
            "name": 'edit_calendar_event',
            "description": 'edit a calendar event',
            "parameters": {
                "type": 'object',
                'properties': {
                    "event_id": {
                        'type': 'integer',
                        'description': 'the associated event id',
                    },
                    'end_time': {
                        'type': 'string',
                        'description': 'datetime for the end of the event',
                    },
                    'summary': {
                        'type': 'string',
                        'description': 'title of the event',
                    },
                    'description': {
                        'type': 'string',
                        'description': 'description of the event including any details that are known',
                    },
                    'start_time': {
                        'type': 'string',
                        'description': 'datetime for the end of the event',
                    },
                },
                'required': ['event_id']
            },

        }
    function_read_calendar_event_with_event_id = {
            "name": 'read_calendar_event_with_event_id',
            "description": 'read a calendar event',
            "parameters": {
                "type": 'object',
                'properties': {
                    "event_id": {
                        'type': 'integer',
                        'description': 'the associated event id',
                    },
                },
                'required': ['event_id']
            },

        }
    function_delete_event = {
            "name": 'delete_event',
            "description": 'delete a calendar event',
            "parameters": {
                "type": 'object',
                'properties': {
                    "event_id": {
                        'type': 'integer',
                        'description': 'the associated event id',
                    }
                },
                'required': ['event_id']
            },

        }
    function_read_events_for_week = {
            "name": 'read_events_for_week',
            "description": 'read a calendar for a week',
            "parameters": {
                "type": 'object',
                'properties': {
                    "date": {
                        'type': 'string',
                        'description': 'datetime for the start of the week',
                    },
                },
                'required': ['date']
            }

        }
    function_read_events_for_day = {
            "name": 'read_events_for_day',
            "description": 'read a calendar for a day',
            "parameters": {
                "type": 'object',
                'properties': {
                    "date": {
                        'type': 'string',
                        'description': 'datetime of the date',
                    },
                },
                'required': ['date']
            }

        }
    function_get_restaurants_in_area = {
        "name": 'get_restaurants_in_area',
        "description": 'get a list of nearby restaurants',
        "parameters": {
            "type": 'object',
            'properties': {
                "latitude": {
                    'type': 'string',
                    'description': 'latitude',
                },
                'longitude': {
                    'type': 'string',
                    'description': 'longitude',
                },
                'radius': {
                    'type': 'integer',
                    'description': 'normal use 500 which is 1 mile unless otherwise asked',
                },
            },
            'required': ['latitude', 'longitude', 'radius']
        }

    }
    function_create_timer = {
        "name": 'create_timer',
        "description": 'create a timer',
        "parameters": {
            "type": 'object',
            'properties': {
                "name": {
                    'type': 'string',
                    'description': 'name of timer',
                },
                'time': {
                    'type': 'string',
                    'description': 'a datetime of when the timer is done',
                },
            },
            'required': ['time']
        }

    }
    function_detect_language = {
        "name": 'detect_language',
        "description": 'detect the language of the text',
        "parameters": {
            "type": 'object',
            'properties': {
                "text": {
                    'type': 'string',
                    'description': 'text of the unknown langauge',
                },
            },
            'required': ['text']
        }

    }
    function_translate_to = {
        "name": 'translate_to',
        "description": 'translate a text to a target language',
        "parameters": {
            "type": 'object',
            'properties': {
                "text": {
                    'type': 'string',
                    'description': 'string of the text that needs to be translated',
                },
                'target_language': {
                    'type': 'string',
                    'description': 'target language',
                },
            },
            'required': ['text', 'target_language']
        }

    }
    function_translate_from = {
        "name": 'translate_from',
        "description": 'translate from a language to english',
        "parameters": {
            "type": 'object',
            'properties': {
                "source_language": {
                    'type': 'string',
                    'description': 'language of the text',
                },
                'text': {
                    'type': 'string',
                    'description': 'the text that needs to be translated',
                },
            },
            'required': ['source_language', 'text']
        }

    }
    function_get_current_weather_city = {
        "name": 'get_current_weather_city',
        "description": 'get the current weather for a city',
        "parameters": {
            "type": 'object',
            'properties': {
                "city": {
                    'type': 'string',
                    'description': 'the city',
                },
            },
            'required': ['city']
        }

    }
    function_get_8day_forecast_city = {
        "name": 'get_8day_forecast_city',
        "description": 'get an 8 day forecast of a city',
        "parameters": {
            "type": 'object',
            'properties': {
                "city": {
                    'type': 'string',
                    'description': 'the city',
                },
            },
            'required': ['city']
        },

    }
    function_turn_lights_on = {
        "name": "turn_lights_on",
        "description": "turns the lights in my house on",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        }
    }
    function_turn_lights_off = {
        "name": "turn_lights_off",
        "description": "turns the lights in my house off",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        }
    }
    function_brightness_up = {
        "name": 'brightness_up',
        "description": 'turns up the brightness of the lights in my house',
        "parameters": {
            "type": 'object',
            "properties": {
                "amount": {
                    'type': 'string',
                    'description': 'the percent brightness',
                }
            },
            "required": ['amount'],
        },

    }
    function_brightness_down = {
        "name": 'brightness_down',
        "description": 'turns down the brightness of the lights in my house',
        "parameters": {
            "type": 'object',
            'properties': {
                "amount": {
                    'type': 'string',
                    'description': 'the percent brightness',
                },
            },
            "required": ['amount'],
        },

    }
    function_set_color = {
        "name": 'set_color',
        "description": 'sets the color of the lights in my house',
        "parameters": {
            "type": 'object',
            'properties': {
                "color": {
                    'type': 'string',
                    'description': 'This hexadecimal of the color the user asked for',
                }
            },
            'required': ['color'],
        }

    }
    function_create_task = {
        "name": 'create_task',
        "description": 'creates a task to do',
        "parameters": {
            "type": 'object',
            'properties': {
                "task_name": {
                    'type': 'string',
                    'description': 'The name of the task',
                },
                "description": {
                    'type': 'string',
                    'description': 'a short description of the task. THIS IS NOT NEEDED',
                },
                "due_date": {
                    'type': 'string',
                    'description': 'ISO format with a datetime of when this task needs to be done by',
                },
                "priority": {
                    'type': 'string',
                    'description': 'the priority level either low, medium or high. THIS IS NOT NEEDED',
                }
            },
            'required': ['task_name', 'due_date'],
        }

    }
    function_set_color = {
        "name": 'set_color',
        "description": 'sets the color of the lights in my house',
        "parameters": {
            "type": 'object',
            'properties': {
                "color": {
                    'type': 'string',
                    'description': 'This hexadecimal of the color the user asked for',
                }
            },
            'required': ['color'],
        }

    }
    function_create_alarm_with_repeat = {
        "name": 'create_alarm_with_repeat',
        "description": 'creates an alarm that repeats',
        "parameters": {
            "type": 'object',
            'properties': {
                "repeat_days": {
                    'type': 'string',
                    'description': 'Names of the days that it repeats EX: "Monday Tuesday"',
                },
                "time": {
                    'type': 'string',
                    'description': 'EX 21:00 MAKE SURE IT HAS A 0 AT beginning EX: 07:30 NOT 7:30',
                }
            },
            'required': ['repeat_days', "time"],
        }
    }
    function_create_alarm_no_repeat = {
        "name": 'create_alarm_no_repeat',
        "description": 'creates an alarm that goes off once',
        "parameters": {
            "type": 'object',
            'properties': {
                "non_repeat_date": {
                    'type': 'string',
                    'description': '(datetime) the date of when alarm should go off in ISO 1801 format',
                },
                "time": {
                    'type': 'string',
                    'description': 'EX 21:00 MAKE SURE IT HAS A 0 AT beginning EX: 07:30 NOT 7:30',
                }
            },
            'required': ['non_repeat_date', "time"],
        }
    }
    function_create_habit = {
        "name": 'create_habit',
        "description": 'creates a habit object',
        "parameters": {
            "type": 'object',
            'properties': {
                "name": {
                    'type': 'string',
                    'description': 'name of the habit',
                },
                "due_time": {
                    'type': 'string',
                    'description': 'time when the habit should be started; EX 21:00 MAKE SURE IT HAS A 0 AT beginning EX: 07:30 NOT 7:30',
                },
                "priority": {
                    'type': 'string',
                    'description': 'either High, Medium, or Low, based of the priority',
                },
                "repeat_days": {
                    'type': 'string',
                    'description': 'name of the day its repeated EX: Monday Tuesday Thursday',
                },
                "description": {
                    'type': 'string',
                    'description': 'description of the habit',
                }
            },
            'required': ['name', "due_time", 'repeat_days'],
        }
    }
    function_explain_all_habits = {
        "name": 'explain_all_habits',
        "description": 'get the information of all habits',
        "parameters": {
            "type": 'object',
            'properties': {
            },
            'required': [],
        }
    }
    function_add_completed_habit = {
        "name": 'add_completed_habit',
        "description": 'if the user completed a habit',
        "parameters": {
            "type": 'object',
            'properties': {
                "habit_id": {
                    'type': 'string',
                    'description': 'id of the habit that was finished',
                }
            },
            'required': ['habit_id'],
        }
    }
    function_select_and_play_album = {
        "name": 'select_and_play_album',
        "description": 'select album for the music, and play it',
        "parameters": {
            "type": 'object',
            'properties': {
                "album_title": {
                    'type': 'string',
                    'description': 'Name of the album',
                }
            },
            'required': ['album_title'],
        }
    }
    function_select_and_play_playlist = {
        "name": 'select_and_play_playlist',
        "description": 'select playlist for the music, and play it',
        "parameters": {
            "type": 'object',
            'properties': {
                "playlist_title": {
                    'type': 'string',
                    'description': 'Title of the playlist',
                }
            },
            'required': ['playlist_title'],
        }
    }
    function_select_and_play_song = {
        "name": 'select_and_play_song',
        "description": 'select song for the music, and play it',
        "parameters": {
            "type": 'object',
            'properties': {
                "song_title": {
                    'type': 'string',
                    'description': 'Title of the song',
                }
            },
            'required': ['song_title'],
        }
    }
    function_select_and_play_artist = {
        "name": 'select_and_play_artist',
        "description": 'select artist for the music, and play it',
        "parameters": {
            "type": 'object',
            'properties': {
                "artist_name": {
                    'type': 'string',
                    'description': 'Name of the artist',
                }
            },
            'required': ['app_name'],
        }
    }
    function_play_music = {
        "name": 'play_music',
        "description": 'play button for the music',
        "parameters": {
            "type": 'object',
            'properties': {
            },
            'required': [],
        }
    }
    function_pause_music = {
        "name": 'pause_music',
        "description": 'pause button for the music',
        "parameters": {
            "type": 'object',
            'properties': {
            },
            'required': [],
        }
    }

    function_skip_track = {
        "name": 'skip_track',
        "description": 'skip button for the music',
        "parameters": {
            "type": 'object',
            'properties': {
            },
            'required': [],
        }
    }
    function_previous_track = {
        "name": 'previous_track',
        "description": 'previous button for the music',
        "parameters": {
            "type": 'object',
            'properties': {
            },
            'required': [],
        }
    }
    function_shuffle_music = {
        "name": 'shuffle_music',
        "description": 'shuffle button for the music',
        "parameters": {
            "type": 'object',
            'properties': {
            },
            'required': [],
        }
    }
    function_repeat_music = {
        "name": 'repeat_music',
        "description": 'repeat button for the music',
        "parameters": {
            "type": 'object',
            'properties': {
            },
            'required': [],
        }
    }
    function_open_app = {
        "name": 'open_app',
        "description": 'opens the specified app',
        "parameters": {
            "type": 'object',
            'properties': {
                "app_name": {
                    'type': 'string',
                    'description': 'name of the app',
                }
            },
            'required': ['app_name'],
        }
    }
    function_send_text_message_with_name = {
        "name": 'send_text_message_with_name',
        "description": 'sends a text message to a contact name',
        "parameters": {
            "type": 'object',
            'properties': {
                "message": {
                    'type': 'string',
                    'description': 'the message to send',
                },
                "contact_name": {
                    'type': 'string',
                    'description': 'name of the contact',
                }

            },
            'required': ['message', 'phone_number'],
        }
    }
    function_send_text_message_with_phone_num = {
        "name": 'send_text_message_with_phone_num',
        "description": 'sends a text message to a phone number',
        "parameters": {
            "type": 'object',
            'properties': {
                "message": {
                    'type': 'string',
                    'description': 'the message to send',
                },
                "phone_number": {
                    'type': 'string',
                    'description': 'phone number of the person',
                }

            },
            'required': ['message', 'phone_number'],
        }
    }
    total_functions: list[dict] = [function_set_color, function_brightness_down, function_brightness_up,
                                   function_turn_lights_off, function_get_8day_forecast_city,
                                   function_get_current_weather_city, function_translate_from, function_translate_to,
                                   function_detect_language, function_create_timer, function_get_restaurants_in_area,
                                   function_read_events_for_day, function_read_events_for_week, function_delete_event,
                                   function_read_calendar_event_with_event_id, function_edit_calendar_event,
                                   function_create_event, function_create_task, function_turn_lights_on,
                                   function_create_alarm_with_repeat, function_create_alarm_no_repeat,
                                   function_create_habit, function_explain_all_habits, function_add_completed_habit,
                                   function_select_and_play_album, function_select_and_play_playlist,
                                   function_select_and_play_song, function_select_and_play_artist,
                                   function_play_music, function_pause_music, function_skip_track,
                                   function_previous_track, function_shuffle_music, function_repeat_music,
                                   function_open_app, function_send_text_message_with_phone_num,
                                   function_send_text_message_with_name
                                   ]
    return total_functions


if __name__ == '__main__':
    get_list_of_functions()
