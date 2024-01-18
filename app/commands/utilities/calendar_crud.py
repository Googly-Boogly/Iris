
#****************************************************#
#  Status: create
#****************************************************#

#****************************************************#
#  Known Bugs: all things with even_id is broken, create_event needs massive changes
#****************************************************#

#++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Requirements: create calendar events, delete calendar events,
#  edit calendar events, read calendar events
#++++++++++++++++++++++++++++++++++++++++++++++++++++#


from datetime import datetime, timedelta, time, date
# from pytz import timezone
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
from global_code.helpful_functions import create_logger_error, log_it, log_exceptions, CustomError
from global_code.secrets import create_calendar_id_google
import os


def create_credentials() -> list:
    pass
    # credentials_path = os.path.join(os.path.dirname(__file__), "../../apis/credentials.json")
    # credentials = service_account.Credentials.from_service_account_file(credentials_path)
    #
    # # Define the desired calendar ID
    # calendar_id = create_calendar_id_google()
    #
    # return [credentials, calendar_id]


@log_exceptions
def create_google_calendar_event(start_time: time, start_date: datetime, end_time: time, end_date: datetime,
                                 summary: str,description: str, timezone_upload: str,
                                 color_id: str or None = None) -> dict:
    """
    calls google calendar api and makes an event
    :param start_time: starting time of the event
    :param start_date: starting date of the event
    :param end_time: ending time of the event
    :param end_date: ending date of the event
    :param summary: title of event
    :param description: description of the event
    :param timezone_upload: the timezone of choice (usually of the location)
    :param color_id: (optional) the id of the color of the event
    :return: returns the result of the api call
    """
    unit_test_create_google_calendar_event(start_time, start_date, end_time, end_date, summary, description,
                                           timezone_upload, color_id)

    # temp1: list[str] = create_credentials()
    # calendar_id = temp1[1]
    # credentials = temp1[0]
    #
    # start_datetime = datetime.combine(start_date, start_time)
    # end_datetime = datetime.combine(end_date, end_time)
    #
    # tz = timezone(timezone_upload)
    #
    # # Convert the start and end datetimes to the desired time zone
    # start_time_tz = tz.localize(start_datetime)
    # end_time_tz = tz.localize(end_datetime)
    #
    # # Convert the start and end times to ISO 8601 format strings
    # start_time_str = start_time_tz.isoformat()
    # end_time_str = end_time_tz.isoformat()
    #
    # service = build('calendar', 'v3', credentials=credentials)
    #
    #
    # event = {
    #     'summary': summary,
    #     'description': description,
    #     'start': {
    #         'dateTime': start_time_str,
    #         'timeZone': timezone_upload,
    #     },
    #     'end': {
    #         'dateTime': end_time_str,
    #         'timeZone': timezone_upload,
    #     },
    # }
    #
    # if color_id:
    #     event['colorId'] = color_id
    #
    # # Call the API to create the event
    # try:
    #     created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
    # except Exception as e:
    #     logger = create_logger_error(os.path.abspath(__file__), 'create_google_calendar_event')
    #     log_it(logger, e)
    #     raise CustomError('GOOGLE CALENDAR API CALL FAILED')
    #
    # # print(f"Event created: {created_event['summary']}")
    # # print(f"Start time: {created_event['start']['dateTime']}")
    # # print(f"End time: {created_event['end']['dateTime']}")
    # return created_event


def unit_test_create_google_calendar_event(start_time: time, start_date: datetime, end_time: time,
                                           end_date: datetime, summary: str,
                                           description: str, timezone_upload: str, color_id: str or None = None):
    """
    unit test for create_google_calendar_event
    :return:
    """
    start_time2 = time(10, 0, 0)
    start_date2 = date(2023, 6, 1)
    end_time2 = time(11, 0, 0)
    end_date2 = date(2023, 6, 1)
    # assert isinstance(start_time, str)
    # assert isinstance(start_date, str)
    # assert isinstance(end_time, str)
    # assert isinstance(end_date, str)
    assert isinstance(summary, str)
    assert isinstance(description, str)
    assert isinstance(timezone_upload, str)
    assert isinstance(color_id, str)
    summary = 'Meeting'
    description = 'Discussion about project updates'
    timezone_upload2 = 'America/Chicago'
    color_id = '4'  # Set the desired color ID here


@log_exceptions
def delete_google_calendar_event(event_id: int) -> dict:
    """
    deletes a google calendar event
    :param event_id: (int) the event id
    :return: returns what the api call returns
    """
    # temp1 = create_credentials()
    # calendar_id = temp1[1]
    # credentials = temp1[0]
    #
    # service = build('calendar', 'v3', credentials=credentials)
    #
    # event = {}
    # # Call the API to delete the event
    # try:
    #     event = service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
    # except Exception as e:
    #     logger = create_logger_error(os.path.abspath(__file__), __name__)
    #     log_it(logger, e)
    #     raise CustomError('GOOGLE CALENDAR API CALL FAILED')
    # finally:
    #     return event


@log_exceptions
def read_event_with_event_id(event_id: int) -> dict:
    """
    reads a google calendar event
    :param event_id: (int) the event id
    :return: (dict) with the summary, description, start time, and end time
    """
    # Load credentials from the JSON file
    # temp1 = create_credentials()
    # calendar_id = temp1[1]
    # credentials = temp1[0]
    #
    # service = build('calendar', 'v3', credentials=credentials)
    #
    # # Call the API to get the event details
    # event = service.events().get(calendarId=calendar_id, eventId=event_id).execute()
    #
    # summary = event['summary']
    # description = event['description']
    # start_time = event['start']['dateTime']
    # end_time = event['end']['dateTime']
    #
    # print(f"""
    # print("Event Details:")
    # print(f"Event ID: {event_id}")
    # print(f"Summary: {summary}")
    # print(f"Description: {description}")
    # print(f"Start Time: {start_time}")
    # print(f"End Time: {end_time}")
    # """)
    # custom_return = {'summary': summary, 'description': description, 'start_time': start_time, 'end_time': end_time}
    # return custom_return


@log_exceptions
def read_events_for_day(date: datetime) -> list:
    """
    reads all events for a specific day
    :param date: (datetime) the date to read events for
    :return: (list) of dictionaries with the event id, summary, description, start time, end time, and color id
    """
    # Load credentials from the JSON file
    # temp1 = create_credentials()
    # calendar_id = temp1[1]
    # credentials = temp1[0]# Build the service object
    # service = build('calendar', 'v3', credentials=credentials)
    #
    # # Construct the start and end datetimes for the specified day
    # start_datetime = datetime.combine(date, datetime.min.time())
    # end_datetime = datetime.combine(date, datetime.max.time())
    #
    # # Convert the start and end times to ISO 8601 format strings
    # start_time_str = start_datetime.isoformat() + 'Z'  # 'Z' indicates UTC time
    # end_time_str = end_datetime.isoformat() + 'Z'  # 'Z' indicates UTC time
    #
    # # Call the API to get the events for the specified day
    # events_result = service.events().list(calendarId=calendar_id, timeMin=start_time_str,
    #                                       timeMax=end_time_str, singleEvents=True).execute()
    # events = events_result.get('items', [])
    #
    # if not events:
    #     raise CustomError('NO EVENTS FOUND')
    # else:
    #     custom_return = []
    #     for event in events:
    #         event_id = event['id']
    #         summary = event['summary']
    #         description = event.get('description', '')
    #         start_time = event['start'].get('dateTime', event['start'].get('date'))
    #         end_time = event['end'].get('dateTime', event['end'].get('date'))
    #         color_id = event.get('colorId', '')
    #
    #         # print(f"""
    #         #     Event ID: {event_id}
    #         #     Summary: {summary}
    #         #     Description: {description}
    #         #     Start Time: {start_time}
    #         #     End Time: {end_time}
    #         #     Color ID: {color_id}
    #         #     """)
    #
    #         custom_return.append({'event_id': event_id, 'summary': summary, 'description': description,
    #                               'start_time': start_time, 'end_time': end_time, 'color_id': color_id})
    #     return custom_return


@log_exceptions
def read_events_for_week(date: datetime) -> list:
    """
    reads all events for a specific week
    :param date: (datetime) the date to read events for
    :return: (list) of dictionaries with the event id, summary, description, start time, end time, and color id
    """
    # temp1 = create_credentials()
    # calendar_id = temp1[1]
    # credentials = temp1[0]
    # service = build('calendar', 'v3', credentials=credentials)
    #
    # end_date = date + timedelta(days=7)
    #
    # # Convert the start and end dates to ISO 8601 format strings
    # start_date_str = date.isoformat() + 'T00:00:00Z'
    # end_date_str = end_date.isoformat() + 'T23:59:59Z'
    #
    # # Query the API for events within the specified week
    # events_result = service.events().list(calendarId=calendar_id, timeMin=start_date_str, timeMax=end_date_str,
    #                                       singleEvents=True, orderBy='startTime').execute()
    # events = events_result.get('items', [])
    # return_events = []
    #
    # if not events:
    #     raise CustomError('NO EVENTS FOUND')
    # else:
    #     for event in events:
    #         event_id = event['id']
    #         event_summary = event['summary']
    #         event_start = event['start'].get('dateTime', event['start'].get('date'))
    #         event_end = event['end'].get('dateTime', event['end'].get('date'))
    #         event_description = event.get('description', '')
    #         event_color_id = event.get('colorId', '')
    #
    #         # print(f"""
    #         #     Event ID: {event_id}
    #         #     Summary: {event_summary}
    #         #     Start: {event_start}
    #         #     End: {event_end}
    #         #     Color ID: {event_color_id}
    #         #     """)
    #         return_events.append({'event_id': event_id, 'summary': event_summary, 'start_time': event_start,
    #                               'end_time': event_end, 'description': event_description, 'color_id': event_color_id})
    #
    # return return_events


@log_exceptions
def edit_calendar_event(event_id: int, summary: str or None = None, description: str or None = None,
                        start_time: datetime or None = None, end_time: datetime or None = None) -> dict:
    """
    edits a single calendar event.
    Will only edit what you pass in every other variable will stay the same
    :param event_id: (int) the event id
    :param summary: (str) title of event
    :param description: (str) description of the event
    :param start_time: (datetime) the start time of the event
    :param end_time: (datetime) the end time of the event
    :return: (dict) with the event id, summary, description, start time, and end time
    """
    # temp1 = create_credentials()
    # calendar_id = temp1[1]
    # credentials = temp1[0]
    # service = build('calendar', 'v3', credentials=credentials)
    #
    # # Retrieve the existing event
    # event = service.events().get(calendarId=calendar_id, eventId=event_id).execute()
    #
    # if summary:
    #     event['summary'] = summary
    # if description:
    #     event['description'] = description
    # if start_time:
    #     event['start'] = {'dateTime': start_time}
    # if end_time:
    #     event['end'] = {'dateTime': end_time}
    #
    # # Call the API to update the event
    # try:
    #     updated_event = service.events().update(calendarId=calendar_id, eventId=event_id, body=event).execute()
    # except Exception as e:
    #     logger = create_logger_error(os.path.abspath(__file__), 'edit_calendar_event')
    #     log_it(logger, e)
    #     raise CustomError('GOOGLE CALENDAR API CALL FAILED')
    # # print(f"""
    # # Event ID: {updated_event['id']}
    # # Summary: {updated_event['summary']}
    # # Description: {updated_event.get('description', '')}
    # # Start Time: {updated_event['start'].get('dateTime', updated_event['start'].get('date'))}
    # # End Time: {updated_event['end'].get('dateTime', updated_event['end'].get('date'))}
    # # """)
    #
    # custom_event = {'event_id': updated_event['id'], 'summary': updated_event['summary'],
    #                 'description': updated_event.get('description', ''),
    #                 'start_time': updated_event['start'].get('dateTime', updated_event['start'].get('date')),
    #                 'end_time': updated_event['end'].get('dateTime', updated_event['end'].get('date'))}
    #
    # return custom_event


if __name__ == '__main__':
    print(datetime.now())
    pass
    # start_time = time(10, 0, 0)
    # start_date = date(2023, 6, 1)
    # end_time = time(11, 0, 0)
    # end_date = date(2023, 6, 1)
    # summary = 'Meeting'
    # description = 'Discussion about project updates'
    # timezone_upload2 = 'America/Chicago'
    # color_id = '4'
    #
    # create_google_calendar_event(start_time, start_date, end_time,
    #                              end_date, summary, description, timezone_upload2, color_id)


# Color id meanings
#1 - Light Purple
#2 - Light Green
#3 - Dark Purple
#4 - Light Red
#5 - Light Yellow
#6 - Dark Orange
#7 - Dark Teal
#8 - Dark Gray
#9 - Dark Blue
#10 - Light Greenish-Gray
#11 - Dark Red

# Read events for a specific day
# date_for_day = date(2023, 6, 2)
# read_events_for_day(date_for_day)
#
# # Read events for a specific week
# start_date_for_week = date(2023, 6, 1)
# read_events_for_week(start_date_for_week)
#
# event_id = '517n8vitr59oiumm9eimqjfs24_20230603'
# new_summary = 'New Summary2'
#
# edit_calendar_event(event_id, summary=new_summary)
#
# delete_event('517n8vitr59oiumm9eimqjfs24_20230603')




