#****************************************************#
#  Status: Not bug tested
#****************************************************#


#++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Requirements: make functions work with only longitiude and latitude
#++++++++++++++++++++++++++++++++++++++++++++++++++++#

# response is too long
# This function will call openweathermap and grab all the data for the specified city, and return a dictonary of the information

from app.global_code.helpful_functions import create_logger_error, log_it, log_exceptions
from app.global_code.secrets import openweathermap_api_key
import requests
import os


@log_exceptions
def get_current_weather_city(city: str) -> dict:
    """
    This function will call openweathermap and grab all the data for the specified city, and return a dictonary of the information
    :param city: the city you want to get the weather for
    :return: a dictionary of the weather information
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": openweathermap_api_key(),
        "units": "metric"  # You can adjust the units as per your preference
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()
    weather_info = {
        "feels_like": weather_data["main"]["feels_like"],
        "humidity": weather_data["main"]["humidity"],
        "pressure": weather_data["main"]["pressure"],
        "temp": weather_data["main"]["temp"],
        "temp_max": weather_data["main"]["temp_max"],
        "temp_min": weather_data["main"]["temp_min"],
        "sunrise": weather_data["sys"]["sunrise"],
        "sunset": weather_data["sys"]["sunset"],
        "visibility": weather_data["visibility"],
        "description": weather_data["weather"][0]["description"],
        "wind_speed": weather_data["wind"]["speed"],
        "wind_deg": weather_data["wind"]["deg"]
    }
    return weather_info


@log_exceptions
def get_8day_forecast_city(city: str) -> list:
    """
    This function will call openweathermap and grab all the data for the specified city,
    and return a list of the information
    :param city: the city you want to get the weather for
    :return: dictionary of the weather information
    """
    base_url = "http://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": openweathermap_api_key(),
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    forecast_data = response.json()
    forecast_info = []

    for forecast in forecast_data["list"]:
        forecast_info.append({
            "feels_like": forecast["main"]["feels_like"],
            "humidity": forecast["main"]["humidity"],
            "pressure": forecast["main"]["pressure"],
            "temp": forecast["main"]["temp"],
            "temp_max": forecast["main"]["temp_max"],
            "temp_min": forecast["main"]["temp_min"],
            "sunrise": forecast["sys"]["sunrise"],
            "sunset": forecast["sys"]["sunset"],
            "visibility": forecast.get("visibility", None),
            "description": forecast["weather"][0]["description"],
            "wind_speed": forecast["wind"]["speed"],
            "wind_deg": forecast["wind"]["deg"]
        })

    return forecast_info


if __name__ == '__main__':
    city = "Minneapolis"
    weather_data = get_current_weather_city(city)
    print(weather_data)
    forecast_data = get_8day_forecast_city(city)
    print(forecast_data)