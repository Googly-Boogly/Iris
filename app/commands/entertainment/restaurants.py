#****************************************************#
#  Status: response is too long
#****************************************************#

import googlemaps
from geopy.distance import geodesic
from app.global_code.helpful_functions import create_logger_error, log_it, log_exceptions, benchmark_and_log_exceptions
import os
from app.global_code.secrets import google_maps_api_key


# This function gets restaurants near the target latitude and longitude in a certain radius this function will return
# a list of dictionaries. the dicts will have address, distance (in miles), the star rating, and the name of the
# restaurant


@benchmark_and_log_exceptions
def get_restaurants_in_area(latitude: float, longitude: float, radius: int) -> list[dict]:
    """
    This function gets restaurants near the target latitude and longitude in a certain radius this function will return
    a list of dictionaries. the dicts will have address, distance (in miles), the star rating, and the name of the
    restaurant
    :param latitude: the latitude of the target location
    :param longitude: the longitude of the target location
    :param radius: radius of circle that the restaurants will be in, (MEASURMENT UNKOWN)
    :return:
    """
    # Initialize the Google Maps client with your API key
    gmaps = googlemaps.Client(key=google_maps_api_key())

    places = gmaps.places_nearby(location=(latitude, longitude), radius=radius, type='restaurant')

    restaurants = []

    for place in places['results']:
        name = place['name']
        address = place['vicinity']
        distance = geodesic((latitude, longitude),
                            (place['geometry']['location']['lat'], place['geometry']['location']['lng'])).miles
        rating = place.get('rating', 0)

        restaurant = {
            'name': name,
            'address': address,
            'distance': distance,
            'rating': rating
        }
        restaurants.append(restaurant)

    return restaurants

if __name__ == '__main__':
    x = get_restaurants_in_area(37.7749, -122.4194, 5000)
    print(x)
