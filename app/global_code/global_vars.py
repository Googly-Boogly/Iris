from datetime import datetime

from app.utils.j_settings import Settings
from app.utils.user_classes import User


def get_current_details() -> Settings:
    user_data = User.select_one(1)
    user_data = user_data[0]

    user = User(
        {'id': 1, 'first_name': user_data['first_name'], 'last_name': user_data['last_name'],
         'middle_name': user_data['middle_name'], 'added': user_data['added'], 'updated': user_data['updated'],
         'email': user_data['email'], 'phone_number': user_data['phone_number'], 'password': user_data['password']}
    )
    setting = Settings(current_latitude=0, current_longitude=0, current_city='test', current_state='test',
                       current_country='test',
                       current_zipcode=55446, current_timezone='test',
                       user=user)
    return setting