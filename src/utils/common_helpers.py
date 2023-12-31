import re
from tabulate import tabulate
import shortuuid
from datetime import datetime
from datetime import date


def generate_uuid() -> int:
    """ This method is used to generate random id of length 4. """

    user_id = int(shortuuid.ShortUUID("123456789").random(4))
    return user_id


def convert_to_datetime_obj(date) -> date:
    """ This method is used to convert a string to datetime object. """
    
    date = datetime.strptime(str(date), "%d/%m/%Y")
    return date


def check_date_diff(date_1: date, date_2: date) -> bool:
    """ This method is used to check difference between two dates. """

    dose_1_date = convert_to_datetime_obj(date_1)
    dose_2_date = convert_to_datetime_obj(date_2)
    date_diff = dose_1_date - dose_2_date
    days = int((date_diff).days)
    if days > 60:
        return True
    else:
        return False


def is_future_date(date: date) -> bool:
    """ This method is used to check if a particular date is future date. """

    date = convert_to_datetime_obj(date)
    today_date = convert_to_datetime_obj((datetime.now()).strftime("%d/%m/%Y"))
    if date > today_date:
        return True
    else:
        return False


def display_table(data: list, headers: list) -> None:
    """ This method is used to display data in tabular format using tabulate. """

    row_id = [i for i in range(1, len(data) + 1)]
    print(tabulate(data, headers=headers, tablefmt="simple_grid"))
